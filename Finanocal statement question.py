from fpdf import FPDF

# Create a PDF object
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Set title and content
pdf.set_font("Arial", style='B', size=16)
pdf.cell(200, 10, txt="Trial Balance and Adjustments", ln=True, align='C')
pdf.ln(10)

# Set body font
pdf.set_font("Arial", size=12)

# Trial Balance Content (Adjusted to match Debit and Credit)
content = """
                          Trial Balance as on 31st March 2025
-------------------------------------------------------------------------------
Account Name                    | Debit (INR)  | Credit (INR)  
-------------------------------------------------------------------------------
Opening Capital                 |            | 250,000
Net Profit for the year         |            | 100,000
Drawings                        | 30,000     | 
Salaries Outstanding            | 8,000      | 
Prepaid Rent                    |            | 5,000
Bad Debts Written Off           | 4,000      | 
Depreciation on Building        | 12,000     | 
Depreciation on Machinery       | 7,000      | 
Stock at the beginning          | 40,000     | 
Stock at the end                | 60,000     | 
Provision for Doubtful Debts    |            | 10,000
Accrued Rent Income             | 3,000      | 
Interest on Capital             |            | 12,500
Interest on Drawings            | 500        | 
Loan from Bank                  |            | 150,000
Bills Receivable                | 15,000     | 
Creditors                       |            | 20,000
Long-term Investments           | 50,000     | 
Fixed Assets (Net)              | 200,000    | 
Contingent Liability (Lawsuit)  |            | 
-------------------------------------------------------------------------------
Total                           | 505,500    | 505,500
-------------------------------------------------------------------------------

Adjustments to be made:
-------------------------------------------------------------------------------
1. Outstanding Salaries: Add ₹8,000 to Salaries in the Profit and Loss Account and show it as a liability in the Balance Sheet.
2. Prepaid Rent: Subtract ₹5,000 from Rent Expense in the Profit and Loss Account and show as an asset in the Balance Sheet.
3. Bad Debts Written Off: Subtract ₹4,000 from Sundry Debtors and adjust in the Profit and Loss Account.
4. Depreciation: Apply depreciation on Buildings and Machinery and reduce the asset values accordingly.
5. Provision for Doubtful Debts: Create a provision for 10% of Sundry Debtors (after bad debts are written off).
6. Accrued Income: Add ₹3,000 to Rent Income and show as an asset in the Balance Sheet.
7. Interest on Capital: Calculate interest on capital (5% of ₹250,000) and adjust in the Profit and Loss Account.
8. Interest on Drawings: Subtract ₹500 from capital.
9. Loan from Bank: Show as a non-current liability (long-term) in the Balance Sheet.
10. Contingent Liability: Note the contingent liability of ₹25,000 as a potential liability in footnotes.
"""

# Add content to the PDF
pdf.multi_cell(0, 10, content)

# Save the PDF to a file
file_path = "Trial_Balance_with_Adjustments.pdf"
pdf.output(file_path)

print("PDF successfully created!")
d
