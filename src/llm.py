import PIL
import google.generativeai as genai


def parse_llm(page, image=False) -> str:
    model = (
        genai.GenerativeModel("gemini-pro-vision")
        if image
        else genai.GenerativeModel("gemini-pro")
    )
    if not image:
        prompt = f"You are a professor. You have to teach a paper to your students. Teach it in a podcast format in a short but detailed way. Here is one page:\n```{page.page_content}```\n"
        return model.generate_content(prompt)

    else:
        ## To be implemented

        # response = llm.generate_content(
        #     [
        #         "Write a short, engaging blog post based on this picture. It should include a description of the meal in the photo and talk about my journey meal prepping.",
        #         img,
        #     ],
        #     stream=True,
        # )
        # response.resolve()
        pass
