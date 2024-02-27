from fastapi import Request
from fastapi.responses import RedirectResponse
from sqladmin import ModelView, BaseView, expose, action

from infrastructure.database.models.users import User
from infrastructure.database.models.error import Error
from infrastructure.database.models.feature import Feature
from infrastructure.database.models.purchase import Purchase


class Users(ModelView, model=User):
    @action(
        name="mailing",
        label="General Mailing",
        add_in_list=True,
    )
    async def send_mailing(self, request: Request):
        return RedirectResponse("/action/enter_message")

    column_list = "__all__"
    can_create = False
    can_export = True
    can_edit = True
    can_delete = True
    name_plural = "Users"
    column_sortable_list = [User.created_at]
    column_searchable_list = [User.user_id]
    export_types = ["csv", "xls"]
    column_labels = {
        User.created_at: "Registration Date",
        User.user_id: "User ID",
        User.username: "Nickname",
        User.full_name: "Full Name",
        User.language_code: "Language",
        User.is_premium: "Premium",
        User.is_bot: "Bot",
    }


class Features(ModelView, model=Feature):
    column_list = "__all__"
    can_create = False
    can_export = True
    can_edit = True
    can_delete = True
    name_plural = "Wishes"
    export_types = ["csv", "xls"]
    column_sortable_list = [Feature.created_at]
    column_searchable_list = [Feature.feature_id, Feature.software]
    column_labels = {
        Feature.feature_id: "Wish ID",
        Feature.user_id: "User ID",
        Feature.software: "Software",
        Feature.created_at: "Message Registration Date",
        Feature.feature_message: "Message",
        Feature.status: "Status",
        Feature.username: "Nickname",
    }


class Errors(ModelView, model=Error):
    column_list = "__all__"
    can_create = False
    can_export = True
    can_edit = True
    can_delete = True
    name_plural = "Errors"
    export_types = ["csv", "xls"]
    column_sortable_list = [Error.created_at]
    column_searchable_list = [Error.error_id, Error.software]
    column_labels = {
        Error.error_id: "Wish ID",
        Error.user_id: "User ID",
        Error.software: "Software",
        Error.created_at: "Message Registration Date",
        Error.error_message: "Message",
        Error.status: "Status",
        Error.username: "Nickname",
    }


class Purchases(ModelView, model=Purchase):
    @action(
        name="mailing",
        label="General Mailing",
        add_in_list=True,
    )
    async def send_mailing(self, request: Request):
        return RedirectResponse("/action/enter_message")

    column_list = "__all__"
    can_create = False
    can_export = True
    can_edit = True
    can_delete = True
    name_plural = "Purchases"
    export_types = ["csv", "xls"]
    column_sortable_list = [Purchase.created_at]
    column_searchable_list = [Purchase.purchase_id, Purchase.software]
    column_labels = {
        Purchase.purchase_id: "Order ID",
        Purchase.user_id: "User ID",
        Purchase.software: "Software",
        Purchase.created_at: "Message Registration Date",
        Purchase.payment_method: "Payment Method",
        Purchase.status: "Status",
        Purchase.username: "Nickname",
    }


class CustomAdmin(BaseView):
    name = "Custom Page"
    icon = ""

    @expose("/custom", methods=["GET"])
    async def test_page(self, request: Request):
        # return await self.templates.TemplateResponse(request, "custom.html")
        return {"status": "life - hard, code - easy"}
