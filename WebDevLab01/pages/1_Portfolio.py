import streamlit as st
import info
import pandas as pd
### About me section

def about_me_section():
    st.header("🚀About Me")
    st.image(info.profile_picture, width = 200)
    st.write(info.about_me) 
    st.write('-----')
about_me_section()


#Sidebar Links
def links():
    st.sidebar.header("Links")
    st.sidebar.text("Follow me on Linkedin!!")
    linkedin_link=f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt="Linkedin" width = "75" height ="75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    st.sidebar.text("Add me for more projects in the future!")
    github_link =f'<a href="{info.my_github_url}"><img src="{info.github_image_url}" alt="Github" width="65" height="65"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    st.sidebar.text("Here's my email for contacting me!")
    email_html =f'<a href="mailto:{info.my_email_address}"><img  src="{info.email_image_url}" alt="Email" width = "75" height ="75"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html =True)
links()


#education

def education(education_data, course_data):
    st.header("📖Education")
    st.subheader(f"**{education_data['Institution']}**")
    st.write(f"**Degree:** {education_data['Degree']}")
    st.write(f"**Graduation Date:** {education_data['Graduation Date']}")
    st.write(f"**GPA:** {education_data['GPA']}")

    st.write("**Relevant Coursework**")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={
        "code": "Course Code",
        "names": "course Names",
        "semester_taken": "Semester Taken",
        "skills" : "What I learned"},
        hide_index=True,
        )
    st.write("---")
education(info.education_data,info.course_data) 


#Professional Experience

def experience(experience_data):
    st.header("💼Professional Experience")
    for job_title, (job_description, image) in experience_data.items():
        expander = st.expander(f"{job_title}")
        expander.image(image,width=250)
        for bullet in job_description:
            expander.write(bullet)
    st.write("---")
experience(info.experience_data)


#project

def project_section(projects_data):
    st.header("🎯Projects")
    for project_name, project_description in projects_data.items():
        expander= st. expander(f"{project_name}")
        expander.write(project_description)
    st.write("---")
project_section(info.projects_data)


##skills

def skills_section(programming_data, spoken_data):
    st.header("🛠️Skills")
    st.subheader("Programming Languages")
    for skill, percentage in programming_data.items():
        st.write(f"{skill}{info.programming_icons.get(skill, '')}")
        st.progress(percentage)
    st.header("Spoken Languages")
    for spoken, proficiency in spoken_data.items():
        st.write(f"{spoken}{info.spoken_icons.get(spoken, '')}: {proficiency}")

    st.write("---")
skills_section(info.programming_data, info.spoken_data)

#Activities

def activites_section(leadership_data, activity_data):
    st.header("🧗Activites")
    tab1,tab2=st.tabs(["Leadership", "Community Service"])
    with tab1:
        st.subheader("🥇Leadership")
        for title, (details,image) in leadership_data.items():
            expander = st.expander(f"{title}")
            expander.image(image, width=250)
            for bullet in details:
                expander.write(bullet)
    with tab2:
        st.subheader("🤝Community Service")
        for title, details in activity_data.items():
            expander = st.expander(f"{title}")
            for bullet in details:
                expander.write(bullet)


    st.write("---")
activites_section(info.leadership_data, info.activity_data)




