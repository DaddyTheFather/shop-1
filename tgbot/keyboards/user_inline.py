from aiogram.utils.keyboard import InlineKeyboardBuilder


class UserKeyboards:
    def menu_keyboard():
        keyboard = InlineKeyboardBuilder()

        keyboard.button(text="💳 Buy", callback_data="translating")
        keyboard.button(
            text="⚠️ Report an error", callback_data="report_error"
        )
        keyboard.button(
            text="💡 Custom Order",
            callback_data="offer_translate",
        )

        keyboard.adjust(1)

        return keyboard.as_markup()

    def software_choices_kb():
        keyboard = InlineKeyboardBuilder()

        keyboard.button(
            text="🐸 Buy SF SEO Spider 19.4",
            callback_data="buy_SF_SEO_Spider_19.4",
        )
        keyboard.button(
            text="🐸 Buy SF SEO Spider 19.2",
            callback_data="buy_SF_SEO_Spider_19.2",
        )
        keyboard.button(
            text="🐸 Buy SF Log File Analyser 6.0",
            callback_data="buy_SF_Log_File_Analyser_6.0",
        )
        keyboard.button(
            text="🐸 Buy SF Log File Analyser 5.3",
            callback_data="buy_SF_Log_File_Analyser_5.3",
        )
        keyboard.button(text="🔙 Back", callback_data="back_software_chs")

        keyboard.adjust(1)

        return keyboard.as_markup()

    def available_softwares_err_kb():
        keyboard = InlineKeyboardBuilder()

        keyboard.button(
            text="🐸 SF SEO Spider 19.4", callback_data="err_SF_SEO_Spider_19.4"
        )
        keyboard.button(
            text="🐸 SF SEO Spider 19.2", callback_data="err_SF_SEO_Spider_19.2"
        )
        keyboard.button(
            text="🐸 SF Log File Analyser 6.0",
            callback_data="err_SF_Log_File_Analyser_6.0",
        )
        keyboard.button(
            text="🐸 SF Log File Analyser 5.3",
            callback_data="err_SF_Log_File_Analyser_5.3",
        )
        keyboard.button(text="🔙 Back", callback_data="back_software_chs")

        keyboard.adjust(1)

        return keyboard.as_markup()

    def available_softwares_fea_kb():
        keyboard = InlineKeyboardBuilder()

        keyboard.button(
            text="🐸 SF SEO Spider 19.4", callback_data="fea_SF_SEO_Spider_19.4"
        )
        keyboard.button(
            text="🐸 SF SEO Spider 19.2", callback_data="fea_SF_SEO_Spider_19.2"
        )
        keyboard.button(
            text="🐸 SF Log File Analyser 6.0",
            callback_data="fea_SF_Log_File_Analyser_6.0",
        )
        keyboard.button(
            text="🐸 SF Log File Analyser 5.3",
            callback_data="fea_SF_Log_File_Analyser_5.3",
        )
        keyboard.button(text="🔙 Back", callback_data="back_software_chs")

        keyboard.adjust(1)

        return keyboard.as_markup()

    def back_keyboard(path: str):
        keyboard = InlineKeyboardBuilder()

        keyboard.button(text="🔙 Back", callback_data=f"soft_{path}")

        return keyboard.as_markup()

    def pay_keyboard():
        keyboard = InlineKeyboardBuilder()

        keyboard.button(text="💳 Pay", callback_data="pay_order")
        keyboard.button(text="🔙 Back", callback_data="back_pay_order")

        return keyboard.as_markup()

    def payments_keyboard():
        keyboard = InlineKeyboardBuilder()

        keyboard.button(
            text="💳 Visa/MasterCard/МИР", callback_data="card"
        )
        keyboard.button(text="💳 Card", callback_data="abroad_card")
        keyboard.button(text="💳 USDT TRC20", callback_data="usdt_trc20")
        keyboard.button(text="🔙 Back", callback_data="back_to_pay")

        keyboard.adjust(1)

        return keyboard.as_markup()
