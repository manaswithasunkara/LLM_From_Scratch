from bs4 import BeautifulSoup
import requests

def decode_secret(url):
    try:
        response= requests.get(url)
        response.raise_for_status()
        soup= BeautifulSoup(response.content, 'html.parser')

        table= soup.find('table')
        if not table:
            print("no table in doc")
            return
        rows= table.find_all('tr')

        grid_data={}
        max_x=0
        max_y=0

        for row in rows[1:]:
            cells= [cell.text.strip() for cell in  row.find_all('td') ]
            if len(cells)<3:
                continue

            try:
                x= int(cells[0])
                char= cells[1]
                y= int(cells[2])
                grid_data[(x, y)] = char

                if max_y<y: max_y=y
                if max_x<x: max_x=x

            except (IndexError,ValueError):
                continue

        for y in range(max_y,-1,-1):
            line=""
            for x in range(max_x+1):
                line+= grid_data.get((x,y)," ")

            print(line)

    except Exception as e:
        print(f"Error: {e}")

if __name__== "__main__":
    user_input= input("Enter a URL:")
    decode_secret(user_input)
