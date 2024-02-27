from aiogram.utils.markdown import bold


class UserMessages:
    def buy_translate_text():
        text = f"""{bold("IMPORTANT! This is only for testing, dont buy anything here!")}

Pricing:
• SF SEO Spider 19.4 — 95 rubles or 1 USDT TRC20;
• SF SEO Spider 19.2 — 95 rubles or 1 USDT TRC20;
• SF Log File Analyser 6.0 — 95 rubles or 1 USDT TRC20;
• SF Log File Analyser 5.3 — 95 rubles or 1 USDT TRC20;
        """

        return text.replace("\\", "")

    def choose_software_text():
        return f"""{bold("Choose one:):")}
• SF SEO Spider 19.4
• SF SEO Spider 19.2
• SF Log File Analyser 6.0
• SF Log File Analyser 5.3
"""

    def instruction_report_text():
        text = f"""{bold("Please describe in free form where you found the error and, if possible, make a screenshot in the form of a link.")}"""

        return text.replace("\\", "")

    def instruction_feature_text():
        text = f"""{bold("Please write in free form your suggestions for improving the translation and, if possible, make a screenshot in the form of a link.")}"""
        return text.replace("\\", "")

    def confirm_payment(chosen_software: str):
        text = f"""You have selected a translation for {bold(chosen_software)}. To proceed with payment, press the “Pay” button"""
        return text.replace("\\", "")

    def confirm_request():
        return "Thank you for your request! It will be reviewed as soon as possible."


class AdminMessages:
    def greet_admin():
        text = f"""{bold("Greetings Admin! Choose an action:")}"""
        return text.replace("\\", "")
