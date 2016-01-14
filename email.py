class EmailTestCase(TestCase):

    def test_attachment(self):
        if getattr(settings, 'TEST_EMAIL_AWS_SES', False):
            settings.EMAIL_BACKEND = 'e_mail.backends.aws_ses.EmailBackend'
            # Prepare email message
            subject, to = 'hello', 'id@hostname.com'
            body = '<h1>This is an important message.</h1>'
            from django.core.mail.message import EmailMessage
            email = EmailMessage(subject=subject, body=body, to=[to])
            email.content_subtype = 'html'
            email.attach_file('/path/to/file.ext')
            email.send()
