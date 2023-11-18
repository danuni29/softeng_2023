import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from bs4 import BeautifulSoup
import requests

app = FastAPI()

@app.get("/")
def menucrawling_func():
    webpage = requests.get("https://sobi.chonbuk.ac.kr/menu/week_menu.php")
    soup = BeautifulSoup(webpage.content, "html.parser")
    restaurants = soup.find_all('h5', {'class': 'title'})

    all_menu_items = []
    menu_by_day = {'월': [], '화': [], '수': [], '목': [], '금': []}

    for restaurant in restaurants:
        restaurant_name = restaurant.text.strip()

        # 원하는 식당이면 해당 식당의 식단을 출력
        if '후생관' in restaurant_name:
            menu = restaurant.find_next('tbody')
            if menu:
                for row in menu.find_all('tr'):
                    # 조식인 경우 건너뛰기
                    if '조식' in row.text:
                        continue
                    if '도시락' in row.text:
                        continue
                    # 각 행의 정보를 출력
                    menu_items = [td.text.strip() for td in row.find_all('td')]
                    all_menu_items.append(menu_items)

    for menu_item in all_menu_items:
        if len(menu_item) == 5:
            for i, day in enumerate(['월', '화', '수', '목', '금']):
                menu_by_day[day].append(menu_item[i])
        else:
            for day in ['월', '화', '수', '목', '금']:
                menu_by_day[day].append(menu_item)

    for day, menu_items in menu_by_day.items():
        cleaned_menu_items = []

        for menu_item in menu_items:
            # '운영없음'이 있으면 제거
            if '운영없음' in menu_item:
                continue

            if isinstance(menu_item, list):
                cleaned_menu_items.extend(menu_item)
            else:
                # '/'로 구분된 문자열을 나누어 개별 아이템으로 만듦
                sub_items = [item.strip() for item in menu_item.split('/')]
                cleaned_menu_items.extend(sub_items)

        # 각 요일에 대한 처리가 끝나면 딕셔너리 업데이트
        menu_by_day[day] = cleaned_menu_items

    return menu_by_day

@app.get("/menu/{day}")
def read_item(day: str):
    # /menu/{day} 경로에 접근했을 때 menucrawling_func에 저장된 결과를 사용하여 해당 요일의 메뉴를 반환
    menu_by_day_result = menucrawling_func()

    # day 파라미터에 해당하는 요일이 있는지 확인하고 해당 메뉴를 반환
    menu = menu_by_day_result.get(day, [])

    if not menu:
        raise HTTPException(status_code=404, detail="Menu not found for the specified day")

    return JSONResponse(content=menu, media_type="application/json", status_code=200)



uvicorn.run(app, host="127.0.0.1", port=8000)

