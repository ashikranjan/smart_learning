from django.core.mail import send_mail


class GoogleSendEmailManager:
    def google_send_email(self, subject, message, email_from, recipient_list):
        try:
            res = send_mail(subject, message, email_from, recipient_list)
            return True
        except Exception as e:
            return False