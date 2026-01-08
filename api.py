import frappe
@frappe.whitelist()
def bulk_insert(doctype, data):
    import json
    if isinstance(data, str): data = json.loads(data)
    for entry in data:
        doc = frappe.get_doc({"doctype": doctype, **entry})
        doc.insert(ignore_permissions=True)
    frappe.db.commit()
    return {"status": "success"}
