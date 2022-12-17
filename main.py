import requests
import bs4

page_num=0

while True :
    try:
        url = f'https://wuzzuf.net/search/jobs/?a=hpb&q=java%20devoloper&start={page_num}'
        result = requests.get(url)
        src = result.content

        soup = bs4.BeautifulSoup(src, "html.parser")

        numder_of_page = int(soup.find("strong").text)




        job_title = []
        company_name = []
        location_name = []
        job_skill = []
        data = []
        time = []


        job_titles = soup.findAll("h2",{"class":"css-m604qf"})
        company_names = soup.findAll("a",{"class":"css-17s97q8"})
        location_names = soup.findAll("span",{"class":"css-5wys0k"})
        job_skills = soup.findAll("div",{"class":"css-y4udm8"})
        posted_new = soup.findAll("div",{"class":"css-4c4ojb"})
        posted_old = soup.findAll("div",{"class":"css-do6t5g"})
        posted = [*posted_new,*posted_old]
        job_time = soup.findAll("div",{"class","css-1lh32fc"})

        for n in range(len(job_titles)) :
            job_title.append(job_titles[n].text)
            company_name.append(company_names[n].text.replace("-",""))
            location_name.append(location_names[n].text)
            job_skill.append(job_skills[n].text.replace("Full Time","").replace("Part Time","").replace("Work From Home",""))
            time.append(job_time[n].text.replace("Work From Home"," Work From Home").replace("Full TimePart Time","Full Time Part Time"))
            data.append(posted[n].text)




        full_list = [job_title,company_name,location_name,time,data,job_skill]
        for all1 in zip(*full_list):
         print(all1)
        page_num += 1
        if (page_num > numder_of_page // 15):
         print("\npages ended, terminate")
         break
        print("\npage switched\n")


    except :

         print("error occurred")
         break
