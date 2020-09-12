import smtplib
try:
    from app.configuration.mail import *
except ImportError:
    print("The mail file could not be found")

import os
import glob
from jinja2 import Environment, FileSystemLoader
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .attachment import Attachment

class Mail:
    """
    :param subject: email subject header
    :param recipients: list of email addresses
    :param body: plain text message
    :param html: HTML message
    :param alts: A dict or an iterable to go through dict() that contains multipart alternatives
    :param sender: email sender address, or **MAIL_DEFAULT_SENDER** by default
    :param cc: CC list
    :param bcc: BCC list
    :param attachments: list of Attachment instances
    :param reply_to: reply-to address
    :param date: send date
    :param charset: message character set
    :param extra_headers: A dictionary of additional headers for the message
    :param mail_options: A list of ESMTP options to be used in MAIL FROM command
    :param rcpt_options:  A list of ESMTP options to be used in RCPT commands

    """
    def __init__(self):
        self.send_from = MAIL_FROM_ADDRESS # set to default as in config
        self.recipients = None
        self.content = None
        self.use_ssl = True
        self.host = self.init_host()
        self.text = ""
        self.html = None
        self.email_charset = 'utf-8'
        self.email_subject = None
        self.current_directory = os.path.abspath(os.getcwd()) + "/app/resources/view/mail"
        self.env = Environment(loader=FileSystemLoader(current_directory))  
        self.env_template = None 
        self.html_attach_property = None
        self.filname = None # path to html file
        self.__reply_to = None
        self.__cc = None
        self.attachments = []


    
    def init_host(self):
        """specify host and login credentials. Any errors with details provided maybe \n
        produced here.
        """
        # if use ssl layer
        if self.use_ssl:
            host = smtplib.SMTP_SSL(MAIL_HOST, MAIL_PORT)
        else:
            host = smtplib.SMTP(MAIL_HOST, MAIL_PORT)

        # if use TLS layer    
        if MAIL_USE_TLS:
            host.starttls()
        
        assert MAIL_USERNAME, "You must provide a username in order to login securely"
        assert MAIL_PASSWORD, "You must provide a password in order to login securely"

        host.login(MAIL_USERNAME, MAIL_PASSWORD)

        return host

    def add_recipient(self, recipient):
        """Adds another recipient to the message.
        :param recipient: email address of recipient.
        """

        if type(self.recipients) == list:
            self.recipients.append(recipient)

        if type(self.recipients) == str:
            temp = self.recipients
            self.recipients = [temp].append(recipient)

    def charset(self, charset):
        """set the character set of this email"""
        self.charset = charset
        return self

    def view(self, filename):
        
        self.env_template = self.env.get_template(filename)
        self.filename = filename
        return self

    def attach(self, filename=None, content_type=None, data=None, disposition=None, headers=None):
        self.attachments.append(Attachment(filename, content_type, data, disposition, headers))

    def via(self, data: dict):
        """replace properties with variable if specified
        :param data: dict dict of variables
        :example: {"name": "foo"}
        """
        self.html_attach_property = data
        self.html = self.env_template.render(self.html_attach_property)

        return self

    def get_template_view(filename):
        templates = glob.glob('*.j2')
        for i in templates:
            if i == filename:
                return True

    @property
    def subject(self):
        return self.email_subject

    @subject.setter
    def subject(self, subject):
        """set email subject"""
        if type(subject) is not str:
            raise TypeError("subject must be a string")
        self.email_subject = subject
        return self
        
    
    def from_sender(self, sender: str):
        """specify the sender email address, default is set to config file \n
        If no sender email address is specified in config file, you may use this \n
        function instead. \n
        Note: this will override the default one
        """
        self.send_from = sender

        return self

    def to(self, recipient):
        """If you wish to specify many recipients, please use array with comma-separated \n
        email address \n

        :param recipient: {string/list}
        """
        self.recipients = recipient

        return self
    
    @property
    def charset(self):
        return self.email_charset

    @charset.setter
    def charset(self, charset):
        self.email_charset = charset
        return self

    def _mimetext(self, text, subtype='plain'):
        """Creates a MIMEText object with the given subtype (default: 'plain')
        If the text is unicode, the utf-8 charset is used.
        """
        charset = self.charset or 'utf-8'
        return MIMEText(text, _subtype=subtype, _charset=charset)

    @property
    def reply_to(self):
        return self.__reply_to
    
    @reply_to.setter
    def reply_to(self, email):
        self.__reply_to = email
        return self
    
    @property
    def cc(self):
        return self.__cc
    
    @cc.setter
    def cc(self, email):
        self.__cc = email
        return self

    def send(self, mailObject=None):
        """send email"""
        if isinstance(mailObject, Mail):
            self.__build_mail_object()

        assert self.recipients, "You must specify a recipient"

        assert self.send_from "You must specify a sender"
        if self.text != None:
            msg = MIMEMultipart()
            msg.attach(self._mimetext(self.text))

        if self.html != None:
            msg = MIMEMultipart('alternative')
            msg.attach(self._mimetext(self.html, "html"))
            if(self.__reply_to):
                msg['reply_to'] = self.__reply_to

            if(self.__cc):
                msg['Cc'] = self.__cc

        if(type(self.recipients) == dict):
            for recipient in self.recipients:
                self.host.sendmail(self.from_sender, recipient, msg.as_string())
        else:
            self.host.sendmail(self.from_sender, self.recipients, msg.as_string())
        self.host.quit()
    
    def line(self, text: str):
        """add text line"""
        if type(text) is not str:
            raise TypeError("Parameter text must be a string", type(text), "is provided")
        if len(self.text) < 0: #if no previous line was entered
            self.text = text
        else:
            self.text = self.text + "\n" + text
        return self
    
    def __build_mail_object(self, mailObject):
        """build mail config from given mail object"""
        mailObject.build()
        self.send_from = mailObject.send_from
        self.recipients = mailObject.recipients
        self.html = mailObject.html
        self.charset = mailObject.charset
        self.subject = mailObject.subject
        self.text = mailObject.text
        
    
    

