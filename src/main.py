import flet as ft


def main(page: ft.Page):

    # ---------------------------------------------------------
    # Page configuration
    # ---------------------------------------------------------

    page.title = "Customer Management System"
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.window.width = 650
    page.window.height = 700
    page.window.resizable = True
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 12

    # Track the customer currently being edited
    editing_customer_id = {"id": None}

    # Keep generating unique IDs during this in-memory stage
    next_customer_id = {"id": 1}

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
    # Table helper
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
            ),
            on_tap=on_cell_tap,
        )

    # ---------------------------------------------------------
    # Customer selection
    # ---------------------------------------------------------

    def on_cell_tap(e):
        clicked_row = e.control.parent

        # Deselect every other row
        for row in customers_table.rows:
            if row != clicked_row:
                row.selected = False

        # Toggle the clicked row
        clicked_row.selected = not clicked_row.selected

        page.update()

    def get_selected_id():
        for row in customers_table.rows:
            if row.selected:
                return row.cells[0].content.content.value

        return None

    # ---------------------------------------------------------
    # Search customers
    # ---------------------------------------------------------

    def handle_search(e):
        search_text = e.control.value.lower()

        for row in customers_table.rows:
            row.visible = False

            for cell in row.cells:
                cell_text = cell.content.content.value.lower()

                if search_text in cell_text:
                    row.visible = True
                    break

        page.update()

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
    # Common dialog functions
    # ---------------------------------------------------------

    def clear_fields():
        name_field.value = ""
        email_field.value = ""
        phone_field.value = ""
        company_field.value = ""

    def close_dialog(e):
        dialog.open = False
        editing_customer_id["id"] = None

        clear_fields()

        page.update()

    # ---------------------------------------------------------
    # Add customer
    # ---------------------------------------------------------

    def open_add_dialog(e):
        editing_customer_id["id"] = None

        dialog.title.value = "Add New Customer"

        clear_fields()

        page.show_dialog(dialog)

    # ---------------------------------------------------------
    # Edit customer
    # ---------------------------------------------------------

    def open_edit_dialog(e):
        selected_id = get_selected_id()

        if selected_id is None:
            return

        for row in customers_table.rows:

            row_id = row.cells[0].content.content.value

            if row_id == selected_id:

                editing_customer_id["id"] = selected_id

                name_field.value = (
                    row.cells[1].content.content.value
                )

                email_field.value = (
                    row.cells[2].content.content.value
                )

                phone_field.value = (
                    row.cells[3].content.content.value
                )

                company_field.value = (
                    row.cells[4].content.content.value
                )

                break

        dialog.title.value = f"Edit Customer #{selected_id}"

        page.show_dialog(dialog)

    # ---------------------------------------------------------
    # Save customer
    # ---------------------------------------------------------

    def save_customer(e):

        # -----------------------------------------------------
        # Edit existing customer
        # -----------------------------------------------------

        if editing_customer_id["id"] is not None:

            target_id = editing_customer_id["id"]

            for row in customers_table.rows:

                row_id = row.cells[0].content.content.value

                if row_id == target_id:

                    row.cells[1].content.content.value = (
                        name_field.value
                    )

                    row.cells[2].content.content.value = (
                        email_field.value
                    )

                    row.cells[3].content.content.value = (
                        phone_field.value
                    )

                    row.cells[4].content.content.value = (
                        company_field.value
                    )

                    break

        # -----------------------------------------------------
        # Add new customer
        # -----------------------------------------------------

        else:

            customer_id = next_customer_id["id"]

            next_customer_id["id"] += 1

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

        # -----------------------------------------------------
        # Finish
        # -----------------------------------------------------

        editing_customer_id["id"] = None

        clear_fields()

        dialog.open = False

        page.update()

    # ---------------------------------------------------------
    # Delete customer
    # ---------------------------------------------------------

    def open_delete_dialog(e):

        selected_id = get_selected_id()

        if selected_id is None:
            return

        confirm_delete_dialog.content.value = (
            f"Are you sure you want to delete "
            f"customer #{selected_id}?"
        )

        page.show_dialog(confirm_delete_dialog)

    def close_delete_dialog(e):

        confirm_delete_dialog.open = False

        page.update()

    def confirm_delete_customer(e):

        selected_id = get_selected_id()

        if selected_id is not None:

            for row in customers_table.rows:

                row_id = row.cells[0].content.content.value

                if row_id == selected_id:

                    customers_table.rows.remove(row)

                    break

        confirm_delete_dialog.open = False

        page.update()

    # ---------------------------------------------------------
    # Add/Edit dialog
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
    # Delete confirmation dialog
    # ---------------------------------------------------------

    confirm_delete_dialog = ft.AlertDialog(
        title=ft.Text("Confirm Delete"),
        content=ft.Text(
            "Are you sure you want to delete this customer?"
        ),
        actions=[
            ft.TextButton(
                "Cancel",
                on_click=close_delete_dialog,
            ),
            ft.TextButton(
                "Yes",
                on_click=confirm_delete_customer,
            ),
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
        content="Add",
        icon=ft.Icons.ADD,
        on_click=open_add_dialog,
    )

    edit_customer_button = ft.Button(
        content="Edit",
        icon=ft.Icons.EDIT,
        on_click=open_edit_dialog,
    )

    delete_customer_button = ft.Button(
        content="Delete",
        icon=ft.Icons.DELETE,
        on_click=open_delete_dialog,
    )

    search_customers = ft.TextField(
        hint_text="Search customers...",
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
        on_change=handle_search,
    )

    # ---------------------------------------------------------
    # Main page layout
    # ---------------------------------------------------------

    page.add(
        ft.Row(
            [
                customers_label,
                ft.Row(
                    [
                        add_customer_button,
                        edit_customer_button,
                        delete_customer_button,
                    ],
                    spacing=8,
                ),
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