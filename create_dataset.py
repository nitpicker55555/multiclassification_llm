import json
import random
import pandas as pd
import openpyxl
from selenium_chatgpt import selenium_spider
xlsx_path=r'C:\Users\Morning\Desktop\hiwi\heart\paper\file_folder\test_folder\副本Geo-AI ethics cases(1).xlsx'
df = pd.read_excel(xlsx_path)
wb = openpyxl.load_workbook(xlsx_path)
def has_values_under_header(header_name):

    sheet = wb.active
    header_row = sheet[1]
    # Find the column index for the given header name
    column_index = None
    for cell in header_row:
        if cell.value == header_name:
            column_index = cell.column
            break

    # If header not found, return False
    if column_index is None:
        return False

    # Check cells under the header for values
    for row in range(2, sheet.max_row + 1):  # Start from 2 to skip header row
        cell_value = sheet.cell(row=row, column=column_index).value
        if cell_value is not None and isinstance(cell_value, (int, float)):  # Check if cell has a number
            return True

    return False
def generate_col():


    sheet = wb.active

    # Get the header row
    header_row = sheet[1]

    # Check for bold columns and store the bold column headers
    bold_column_headers = [cell.value for cell in header_row if cell.font.bold]
    # Get indices of the bold columns
    bold_column_indices = [cell.column for cell in header_row if cell.font.bold]

    # Create a dictionary to store headers between bold columns
    corrected_headers_between_bold = {}

    # Iterate over the bold column indices and extract headers between them
    for idx, bold_index in enumerate(bold_column_indices[:-1]):
        next_bold_index = bold_column_indices[idx + 1]
        headers_between = [header_row[i].value for i in range(bold_index, next_bold_index-1)]
        corrected_headers_between_bold[header_row[bold_index-1].value] = headers_between

    print(corrected_headers_between_bold)
    return corrected_headers_between_bold


# for col in corrected_headers_between_bold:

# if has_values_under_header(col) 后面的键值在键名成立后才考虑
economic_loss={1:'''• A slight economic loss that may equal or slightly exceed daily expenses. • Losses can be recovered quickly without affecting the overall financial condition of the individual or organization.
• For example, loss of small consumer goods or minor investment losses.
''',
                2:'''
Smaller financial losses, but beyond daily budget, may require financial adjustments.
It may take some time to recoup these losses, but there may not be a serious impact on the financial health of the individual or organization in the long run.
For example, damage or loss to an item of moderate value, or the failure of a small investment.
'''
                ,3:"""
                • Significant financial losses, which may require significant financial adjustments or changes in strategy.
• For individuals, it may mean losing months of income or significant savings.
• For the organization, it may affect some business operations or cause some projects to fail.
• For example, the failure of a large investment or the loss of an important asset.
                """,
                4:"""
                • Extreme financial losses that may threaten the long-term financial health of an individual or the continued operations of an organization.
• For individuals, it may mean losing several years of income, or a significant portion of life savings.
• For organizations, it may result in mass layoffs, business contraction, or bankruptcy.
• For example, the bankruptcy of a large business or the complete failure of a critical project.
                """,5:"""
                • An absolute economic disaster from which recovery is almost impossible.
• For individuals, it may lead to lifelong poverty or the inability to maintain basic necessities of life.
• For an organization, means outright bankruptcy or dissolution.
• For example, the loss of all an individual's assets, or the complete collapse of a global business.
"""}
physical_harm={1:'''• • Minor scratches or abrasions that do not require medical intervention.
• No ongoing pain or discomfort.
• Natural recovery is fully expected within a short period of time.

''',
                2:'''
Some minor injuries:
• Superficial cuts, bruises, or minor strains.
• Basic home treatments may be needed, such as disinfecting or applying a band-aid.
• Recovery can be expected within a week.

'''
                ,3:"""
                • • Visible physical injury such as broken bones, burns, or severe cuts.
• Medical intervention may be required, such as suturing wounds or fixing fractures.
• Recovery may take a period of time, with potential long-term effects, but full or partial recovery is generally expected.

                """,
                4:"""
• Causes major organ damage or loss of function, such as severe concussion or blindness.
• Requires immediate and ongoing medical intervention.
• May have lasting physical impairments or require lengthy rehabilitation.

                """,5:"""
• Injuries that are directly fatal or cause imminent death.
• Causes permanent serious injuries such as high degree of paraplegia.
• Completely and permanently alters the individual's quality of life and cannot return to pre-injury conditions.

"""}
discrimination={1:'''• • • Prejudice based on unconscious, non-malicious, everyday minor misunderstandings or beliefs.
• Does not involve any explicit discriminatory behavior or remarks.
• The person being discriminated against may not know or feel that they are being discriminated against.


''',
                2:'''
• Comments or actions based on stereotypes are, may cause some discomfort but are not sustained or deep.
• In the workplace or social settings, there may be mild rejection or neglect.
• The person being discriminated against feels mildly upset or confused.

'''
                ,3:"""
• Long-term, systemic unequal treatment, such as unfair promotion or pay in the workplace.
• Explicit insult or humiliation based on race, gender, religion or other identity characteristics.
• People who have been discriminated against may experience severe emotional harm, damaged self-esteem or social isolation.
                """,
                4:"""
• Experiencing physical violence or threats, such as racial or religious hate crimes.
• Being explicitly and openly excluded or isolated, such as being discriminated against in the community.
• Seriously affects the quality of life, economic status or personal safety of the person being discriminated against.

                """,5:"""
• Cause serious bodily injury or death.
• Institutionalized discrimination at a social or national level, such as ethnic cleansing or apartheid.
• Complete deprivation of basic human rights and dignity of those discriminated against, resulting in long-term psychological, social and material deprivation.


"""}
privacy_violation={1:'''
• • Violated information is data that is publicly available or widely known, such as public social media profile information.
• The information is insufficient to be used for fraud or identity theft.
• Will not result in any form of discrimination or negative impact.


''',
                2:'''
• The leaked information may be used for harmless commercial purposes, such as advertising.
• May receive unwanted spam or phone calls.
• Mild privacy concerns, but no long-term effects


'''
                ,3:"""
• The leaked information could be used for targeted advertising or other more intrusive marketing strategies.
• Be used for demographic profiling that may result in unfair price discrimination or other forms of discrimination.
• Causes moderate social or psychological distress.


                """,
                4:"""
• Leaked information, such as health data or biometric data, could be used for discrimination, fraud, or other illegal activities.
• Result in identity theft and possible financial loss.
• Cause long-term social distrust or psychological stress.


                """,5:"""
• Disclosure of information, such as about a person's sexual life, political opinions or religious beliefs, could lead to extreme discrimination, social ostracism or violence.
• A direct threat to an individual's safety, liberty, or quality of life.
• Long-term and irreparable social, economic or psychological harm.


"""}
mental_harm={1:'''• • • Mildly unpleasant, probably quickly forgotten.
• Brief mood changes, such as momentary surprise or disappointment.
• No outside intervention or psychological assistance is required.
''',
                2:'''
• Temporary anxiety, irritability, or sadness that does not interfere with daily life.
• is sad about the event, but able to adjust.
• May avoid certain incident-related situations briefly, but not long-term.
'''
                ,3:"""
• Persistent low mood or anxiety that takes some time to recover from.
• You may need to communicate with family and friends to deal with it or seek psychological assistance.
• Persistent avoidance of certain incident-related situations.
• May temporarily affect daily functions or work.
                """,
                4:"""
• Persistent, intense negative emotions such as hopelessness and deep anxiety.
• Professional psychotherapy or counseling is required.
• Intense and chronic avoidance of situations related to the incident.
• Significantly affects daily functions such as work, school, or relationships.
                """,5:"""
• Extreme emotional pain, such as deep depression, intense anxiety, or feelings of hopelessness.
• Suicidal thoughts or tendencies toward self-harm may occur.
• Severe interference with daily life and functioning, may require emergency intervention or hospitalization.
• Inability to recover from the event over an extended period of time, with lasting and profound effects on quality of life.

"""}
def create_data():
    for i in range(40):

        result_dict = generate_col()

        final_dict={}
        question = ""



        for bold_col in result_dict:

            if has_values_under_header(bold_col): #有实际意义的col


                bold_attribute = True if random.random() < 0.5 else False
                final_dict[bold_col] = bold_attribute
                if bold_attribute:
                    if "extent of impact is Identified" in bold_col:
                        question += "%s is True，extent of impact is" % random.choice(result_dict[bold_col])
                    else:
                        question += "%s is True，Detailed rules are as follows:" % bold_col
                        for element in result_dict[bold_col]:

                            if "severity" in element:
                                attribute_value = random.choice([1, 2, 3, 4, 5])
                                question+="%s is \n %s，"%(element, globals().get(str(element).replace("severity of ","").replace(" ",'_').lower())[attribute_value])


                            else:

                                attribute_value = True if random.random() < 0.5 else False
                                question += "%s is %s，"%(element, attribute_value)
                            final_dict[element] = attribute_value


            else:

                question += "\nUnder the topic %s, Detailed rules are as follows:" % bold_col
                for element in result_dict[bold_col]:
                    if "severity" in element:
                        attribute_value = random.choice([1, 2, 3, 4, 5])
                        question += "%s is  \n %s，" % (element, globals().get(
                            str(element).replace("severity of ", "").replace(" ", '_').lower())[attribute_value])


                    else:

                        attribute_value = True if random.random() < 0.5 else False

                        question += "%s is %s，" % (element, attribute_value)
                    final_dict[element] = attribute_value
                    if bold_col=="Data Production Process":
                        question+="Those are all the rules. Please output a news item and do not explicitly display the rules I sent you."
        if i==0:
            selenium_spider("", False, True, "4")
            selenium_spider(
                "I want you to help me generate news about AI accidents in a seroius news style.After I give you specific rules,Please write down the specific accidents that may cause these problems according to the rules I gave, and describe the specific consequences of these accidents in detail, such as what bad consequences were caused and the specific details of these consequences. Details and what are the causes of these consequences, rather than explicitly stating the rules I gave. The output format should be json,like {'News Title':{},'Content':{}}  If you understand, please reply ok")

            result=(selenium_spider(question,True,False,"4"))
        else:
            result=(selenium_spider(question,False,False,"4"))
        print(result)

        print("=========")
        print(final_dict)
        print(result)
        json_dict={"attribute":final_dict,"news":result}
        with open("output.jsonl", "a", encoding='utf-8') as f:

                f.write(json.dumps(json_dict) + "\n")


def checking_layer():
    description_list=df["Description"].fillna("", inplace=True)
    result_dict = generate_col()
    detailed_description_list=df["Detailed Description"].fillna("", inplace=True)
    for num, element in enumerate(description_list):
        case_str=element+detailed_description_list[num]
        selenium_spider(case_str+", according to the case above, please answer my question below with yes or no.")




        final_dict = {}
        question = ""

        for bold_col in result_dict:

            if has_values_under_header(bold_col):  # 有实际意义的col


                final_dict[bold_col] = bold_attribute
                if bold_attribute:
                    if "extent of impact is Identified" in bold_col:
                        question += "%s is True，extent of impact is" % random.choice(result_dict[bold_col])
                    else:
                        question += "%s is True，Detailed rules are as follows:" % bold_col
                        for element in result_dict[bold_col]:

                            if "severity" in element:
                                attribute_value = random.choice([1, 2, 3, 4, 5])
                                question += "%s is \n %s，" % (element, globals().get(
                                    str(element).replace("severity of ", "").replace(" ", '_').lower())[
                                    attribute_value])


                            else:

                                attribute_value = True if random.random() < 0.5 else False
                                question += "%s is %s，" % (element, attribute_value)
                            final_dict[element] = attribute_value


            else:

                question += "\nUnder the topic %s, Detailed rules are as follows:" % bold_col
                for element in result_dict[bold_col]:
                    if "severity" in element:
                        attribute_value = random.choice([1, 2, 3, 4, 5])
                        question += "%s is  \n %s，" % (element, globals().get(
                            str(element).replace("severity of ", "").replace(" ", '_').lower())[attribute_value])


                    else:

                        attribute_value = True if random.random() < 0.5 else False

                        question += "%s is %s，" % (element, attribute_value)
                    final_dict[element] = attribute_value
                    if bold_col == "Data Production Process":
                        question += "Those are all the rules. Please output a news item and do not explicitly display the rules I sent you."

        json_dict = {"attribute": final_dict, "news": result}
        with open("output.jsonl", "a", encoding='utf-8') as f:

            f.write(json.dumps(json_dict) + "\n")
create_data()
# checking_layer()