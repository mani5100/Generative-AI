from langchain_core.prompts import PromptTemplate
prompt_template=PromptTemplate(template="""
                      Please summerize the research paper titled {user_input_paper} with the following style.
                      Explaination Style : {user_exp_style}
                      Explanation Length: {user_exp_length}
                      1. Insclude Methametical Equations if available in paper and explain those methematical concepts using simple and intutive code snippets where applicable. 
                      2. Use relatable analogies to explain complex ideas.
                      If certain information is not available the respond with "Insufficient Information available" rather then guessing it.
                      Ensure summaery is clear, accurate and alogned with provided style and length.
                      """,
                      input_variables=['user_input_paper','user_exp_style','user_exp_length'],
                      validate_template=True)
prompt_template.save("Prompts/PromptTemplate.json")