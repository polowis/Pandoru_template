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
from email.mime.application import MIMEApplication
from .attachment import Attachment
from email.utils import formatdate
from email.mime.image import MIMEImage
import time
from .exception import InvalidBodyText

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
        self._html = None
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
        self.date = time.time()
        self.msg = None


    
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
        self.email_charset = charset
        return self
    
    def html(self, html):
        """Inject html code \n
        """
        if isinstance(html, str):
            self._html = html
        else:
            raise TypeError("html must be a string")
        return self

    def view(self, filename):
        """attach a HTML layout to this email"""
        self.env_template = self.env.get_template(filename)
        self.filename = filename
        return self

    def set_view_directory(self, directory_path):
        """set the path to the folder containing the view of the email \n
        :param directory_path: path to the directory
        """
        self.current_directory = directory_path
        return self

    def attach_from_disk(self, filename=None, options={}):
        """attach a file
        :param filename: path to file
        :param option: option to be passed
        """
        if filename is not str:
            raise TypeError("Filename must be a string")
        self.attachments.append(Attachment(filename, data=options))

    def __bad_subject(self):
        """check for bad subject, such as new line in subject"""
        return '\n' in self.email_subject or '\r' in self.email_subject:

    def attach(self, data: dict):
        """replace properties with variable if specified
        :param data: dict dict of variables
        :example: {"name": "foo"}
        """
        self.html_attach_property = data

        return self

    def get_template_view(filename):
        templates = glob.glob('*.j2')
        for i in templates:
            if i == filename:
                return True

    def subject(self, subj):
        """set email subject"""
       self.email_subject = subj
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

   
    def reply_to(self, email):
        self.__reply_to = email
        return self
    
    def cc(self, email):
        self.__cc = email
        return self

    def send(self, mailObject=None):
        """send email"""
        if isinstance(mailObject, Mail):
            self.__build_mail_object()

        assert self.recipients, "You must specify a recipient"

        assert self.send_from "You must specify a sender"

        # if no body provided
        if self.text == None and self._html == None and len(self.attachments) == 0:
            raise Exception("You need to provide the body for the email. Email cannot be blank")

        # check if only plain text and no attachments
        if self.text != None and len(self.attachments) == 0:
            self.msg = self._mimetext(self.text)

        elif len(self.attachments) > 0 and self._html == None:
            self.msg = MIMEMultipart()
            self.msg.attach(self._mimetext(self.text))

        else:
            self.msg = MIMEMultipart('alternative')
            self.msg.attach(self._mimetext(self._html, "html"))
        
        if self.email_subject:
            if self.__bad_subject():
                raise InvalidBodyText("Invalid email subject, email subject should not contain any new line")
            self.msg['Subject'] = self.email_subject

        self._build_cc()._build_reply_to()._build_date()

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
        self._html = mailObject._html
        self.charset = mailObject.charset
        self.subject = mailObject.subject
        self.text = mailObject.text
    
    def __build_mail_subject(self, subject: str):
        """build mail subject"""
        if type(subject) is not None and is not str:
            raise TypeError("subject must be a string")
        if  self.__bad_subject():
                raise Exception("Invalid email subject, email subject should not contain any new line")
        self.email_subject = subject
        return self

    def _build_cc(self, address: str):
        """Set the recipients of the message."""
        if self.__cc:
            self.msg['Cc'] = self.__cc
            return self
        return self
    
    def _build_reply_to(self, address: str):
        """Set the reply-to address of the message"""
        if self.__reply_to:
            self.msg['Reply_to'] = self.__reply_to
            return self
        return self

    def _build_view(self):
        self._html = self.env_template.render(self.html_attach_property)
        return self

    def __set_address(self, address: str, name = None, category):
        """set address where the email is sent"""
        if category == "cc":
            return self.__cc = address
        elif category == "reply_to":
            return self.__reply_to = address
    
    def _build_date(self):
        """set date for the email"""
        self.msg['Date'] = formatdate(self.date, localtime=True)
        return True
    
    def _add_attachments(self):
        """add attachments to email"""
        for attachment in self.attachments or []:
            with open(attachment.path, 'rb') as file:
                if attachment.extension in ['.png', '.jpg']:
                    file_to_attach = MIMEImage(file.read())
                else:
                    file_to_attach = MIMEApplication(file.read(), Name=attachment.name)
                file_to_attach.add_header('content-disposition', attachment.disposition, filename=attachment.filename)
            self.msg.attach(file_to_attach)

    
        
    