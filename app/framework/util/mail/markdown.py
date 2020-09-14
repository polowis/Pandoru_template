from bs4 import BeautifulSoup
import markdown

class Markdown:
    def __init__(self, markdown_content=None, options=None):
        self.path = options.get('path')
        self.current_dir = options.get('current_dir', '')
        self._css = options.get('css')

        self.markdown_content = markdown_content

        self._md = markdown.Markdown(extensions=[
            'markdown.extensions.tables',
            'markdown.extensions.meta'])
        self._html = None
        self._images = None
    
    def _convert_markdown(self):
        if self.markdown_content:
            self._html = markdown.markdown(self.markdown_content)
        if self.path is not None:
            with open(self.path, "r", encoding="utf-8") as input_file:
                text = input_file.read()
            self._html = text
        return self._html

    def convert(self):
        self._convert_markdown()
        content = self._insert_html()

        if self._css is not None:
            self._insert_css(content)

    def _insert_html(self):
        email_html_template = u"""
        <!doctype html>
        <html>
            <head>
                <meta charset="UTF-8">
                <style>

                </style>
            </head>
            <body>
                {content}
            </body>
        </html>"""
        return email_html_template.format(content=self._html)

    def _insert_css(self, content):
        soup = BeautifulSoup(content)
        if isinstance(self._css, dict):
            for css_file in self._css:
                tag = soup.new_tag("link")
                tag.attrs['href'] = css_file
                soup.head.insert(0, tag)
        else:
            raise TypeError("Css links must be a dict")
        
