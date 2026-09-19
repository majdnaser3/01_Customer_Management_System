import flet as ft


def main(page: ft.Page):

    # ---------------------------------------------------------
    # Page configuration
    # ---------------------------------------------------------

    page.title = "Customer Management System"
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.window.width = 500
    page.window.height = 700
    page.window.resizable = True
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 12

    # ---------------------------------------------------------
    # Helper for table cells
    # ---------------------------------------------------------

    def create_cell(text, width):
        return ft.DataCell(
            ft.Container(
                width=width,
                content=ft.Text(
                    str(text),
                    max_lines=1,
                    overflow=ft.TextOverflow.ELLIPSIS,
                ),
            )
        )

    # ---------------------------------------------------------
    # Customer table
    # ---------------------------------------------------------

    customers_table = ft.DataTable(
        columns=[
            ft.DataColumn(
                ft.Container(
                    width=40,
                    content=ft.Text("ID"),
                )
            ),
            ft.DataColumn(
                ft.Container(
                    width=90,
                    content=ft.Text("Name"),
                )
            ),
            ft.DataColumn(
                ft.Container(
                    width=120,
                    content=ft.Text("Email"),
                )
            ),
            ft.DataColumn(
                ft.Container(
                    width=90,
                    content=ft.Text("Phone"),
                )
            ),
            ft.DataColumn(
                ft.Container(
                    width=100,
                    content=ft.Text("Company"),
                )
            ),
        ],
        rows=[],
        heading_row_height=40,
        column_spacing=10,
        border=ft.Border.all(1, ft.Colors.WHITE),
        horizontal_lines=ft.BorderSide(1, ft.Colors.WHITE),
        vertical_lines=ft.BorderSide(1, ft.Colors.WHITE),
    )

    # ---------------------------------------------------------
    # Dialog fields
    # ---------------------------------------------------------

    name_field = ft.TextField(
        label="Name",
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
    )

    email_field = ft.TextField(
        label="Email",
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
    )

    phone_field = ft.TextField(
        label="Phone",
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
    )

    company_field = ft.TextField(
        label="Company",
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
    )

    # ---------------------------------------------------------
    # Dialog functions
    # ---------------------------------------------------------

    def close_dialog(e):
        dialog.open = False
        page.update()

    def save_customer(e):

        customer_id = len(customers_table.rows) + 1

        new_row = ft.DataRow(
            cells=[
                create_cell(customer_id, 40),
                create_cell(name_field.value, 90),
                create_cell(email_field.value, 120),
                create_cell(phone_field.value, 90),
                create_cell(company_field.value, 100),
            ]
        )

        customers_table.rows.append(new_row)

        # Clear fields for the next customer
        name_field.value = ""
        email_field.value = ""
        phone_field.value = ""
        company_field.value = ""

        dialog.open = False
        page.update()

    def open_dialog(e):
        page.show_dialog(dialog)

    # ---------------------------------------------------------
    # Dialog
    # ---------------------------------------------------------

    cancel_button = ft.TextButton(
        "Cancel",
        on_click=close_dialog,
    )

    save_button = ft.TextButton(
        "Save",
        on_click=save_customer,
    )

    dialog = ft.AlertDialog(
        title=ft.Text("Add New Customer"),
        content=ft.Column(
            [
                name_field,
                email_field,
                phone_field,
                company_field,
            ]
        ),
        actions=[
            cancel_button,
            save_button,
        ],
    )

    # ---------------------------------------------------------
    # Main page controls
    # ---------------------------------------------------------

    customers_label = ft.Text(
        value="Customers",
        size=30,
        weight="bold",
    )

    add_customer_button = ft.Button(
        content="Add Customer",
        icon=ft.Icons.ADD,
        on_click=open_dialog,
    )

    search_customers = ft.TextField(
        hint_text="Search customers...",
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
    )

    # ---------------------------------------------------------
    # Main page layout
    # ---------------------------------------------------------

    page.add(
        ft.Row(
            [
                customers_label,
                add_customer_button,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),

        ft.Divider(height=20),

        search_customers,

        ft.Divider(height=20),

        customers_table,
    )


if __name__ == "__main__":
    ft.run(main)