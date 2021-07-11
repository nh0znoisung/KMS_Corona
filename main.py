import asyncio

import cv2
import numpy as np
import websockets
import base64
import json
import os

CORONA_TEMPLATE_PATH = os.path.dirname(os.path.abspath(__file__)) + '\\corona_template.png'
CORONA_TEMPLATE_1 = os.path.dirname(os.path.abspath(__file__)) + '\\corona_template_1.png'
CORONA_TEMPLATE_2 = os.path.dirname(os.path.abspath(__file__)) + '\\corona_template_2.png'
CORONA_TEMPLATE_3 = os.path.dirname(os.path.abspath(__file__)) + '\\corona_template_3.png'
CORONA_TEMPLATE_4 = os.path.dirname(os.path.abspath(__file__)) + '\\corona_template_4.png'

# CORONA_1 = os.path.dirname(os.path.abspath(__file__)) + '\\characters\\character-1.png' # 2
# CORONA_2 = os.path.dirname(os.path.abspath(__file__)) + '\\characters\\character-2.png' # 4
# CORONA_3 = os.path.dirname(os.path.abspath(__file__)) + '\\characters\\character-3.png' # 6
# CORONA_4 = os.path.dirname(os.path.abspath(__file__)) + '\\characters\\character-4.png' # 10
# CORONA_5 = os.path.dirname(os.path.abspath(__file__)) + '\\characters\\character-5.png' # -20
# CORONA_6 = os.path.dirname(os.path.abspath(__file__)) + '\\characters\\character-6.png' # -All

CORONA_SCALE_RATIO = 0.5
CORONA_SCALE = 0.375

corona_template_image = cv2.imread(CORONA_TEMPLATE_PATH, 0)
corona_template_image = cv2.resize(corona_template_image, None, fx=CORONA_SCALE_RATIO, fy=CORONA_SCALE_RATIO)

Corona_template_1 = cv2.imread(CORONA_TEMPLATE_1, 0)
corona_template_1 = cv2.resize(Corona_template_1, None, fx=CORONA_SCALE_RATIO, fy=CORONA_SCALE_RATIO)
corona_template_1_1 = cv2.resize(Corona_template_1, dsize=(80,80))

Corona_template_2 = cv2.imread(CORONA_TEMPLATE_2, 0)
corona_template_2 = cv2.resize(Corona_template_2, None, fx=CORONA_SCALE_RATIO, fy=CORONA_SCALE_RATIO)
corona_template_2_1 = cv2.resize(Corona_template_2, dsize=(80,80))

Corona_template_3 = cv2.imread(CORONA_TEMPLATE_3, 0)
corona_template_3 = cv2.resize(Corona_template_3, None, fx=CORONA_SCALE_RATIO, fy=CORONA_SCALE_RATIO)
corona_template_3_1 = cv2.resize(Corona_template_3, dsize=(80,80))

Corona_template_4 = cv2.imread(CORONA_TEMPLATE_4, 0)
corona_template_4 = cv2.resize(Corona_template_4, dsize=(100,100))
corona_template_4_1 = cv2.resize(Corona_template_4, dsize=(80,80))



# def catch_corona(wave_image, threshold=0.75):
#     wave_image_gray = cv2.cvtColor(wave_image, cv2.COLOR_BGRA2GRAY)
#     # corona_template_image
#     # 200x200 -> 80x80
#     res = cv2.matchTemplate(wave_image_gray, corona_template_4, cv2.TM_CCOEFF_NORMED)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

#     if max_val < threshold:
#         return []

#     # 190 x 196:2
#     width, height = corona_template_image.shape[::-1]
#     top_left = max_loc
#     bottom_right = (top_left[0] + width, top_left[1] + height)

#     return [[top_left, bottom_right]]


# def catch_corona(wave_image, threshold=0.75):
#     wave_image_gray = cv2.cvtColor(wave_image, cv2.COLOR_BGRA2GRAY)
#     # corona_template_image
#     # 200x200 -> 80x80
#     ans = []
#     ok = 0
#     for i in range(80, 201, step_pixel):
#         if ok == 1:
#             break
#         corona_template_4 = cv2.resize(Corona_template_4, dsize=(i,i))
#         res = cv2.matchTemplate(wave_image_gray, corona_template_4, cv2.TM_CCOEFF_NORMED)
#         min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
#         if max_val >= threshold:
#             width, height = corona_template_image.shape[::-1]
#             top_left = max_loc
#             bottom_right = (top_left[0] + width, top_left[1] + height)
#             ok = 1
#             ans.append([top_left, bottom_right])

#     return ans

# step_pixel = 40
list_pixel = [90, 120]
# def catch_corona(wave_image, threshold=0.76):
    # wave_image_gray = cv2.cvtColor(wave_image, cv2.COLOR_BGRA2GRAY)

    # ans = []
    # list_template = [Corona_template_1, Corona_template_2, Corona_template_3, Corona_template_4]
    # for corona_template in list_template:
    #     for i in list_pixel:
    #         corona = cv2.resize(corona_template, dsize=(i,i))
    #         res = cv2.matchTemplate(wave_image_gray, corona, cv2.TM_CCOEFF_NORMED)
    #         min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        
    #         if max_val >= threshold:
    #             top_left = max_loc
    #             bottom_right = (top_left[0] + i, top_left[1] + i)
    #             ans.append([top_left, bottom_right])
    # return ans




def catch_corona(wave_image, threshold=0.76):
    wave_image_gray = cv2.cvtColor(wave_image, cv2.COLOR_BGRA2GRAY)

    width, height = corona_template_image.shape[::-1]
    ans = []
    list_template = [corona_template_1, corona_template_2, corona_template_3, corona_template_4]
    for corona_template in list_template:
        res = cv2.matchTemplate(wave_image_gray, corona_template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if max_val >= threshold:
            top_left = max_loc
            bottom_right = (top_left[0] + width, top_left[1] + height)
            ans.append([top_left, bottom_right])

    # list_template_1 = [corona_template_1_1, corona_template_2_1, corona_template_3_1, corona_template_4_1]  
    # for corona_template in list_template_1:
    #     res = cv2.matchTemplate(wave_image_gray, corona_template, cv2.TM_CCOEFF_NORMED)
    #     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    #     if max_val >= threshold:
    #         top_left = max_loc
    #         bottom_right = (top_left[0] + 80, top_left[1] + 80)
    #         ans.append([top_left, bottom_right])

    return ans


## Too much dangerous
# def catch_corona(wave_image, threshold=0.81):
#     wave_image_gray = cv2.cvtColor(wave_image, cv2.COLOR_BGRA2GRAY)

#     width, height = corona_template_image.shape[::-1]
#     ans = []
#     list_template = [corona_template_1, corona_template_2, corona_template_3, corona_template_4]
#     for corona_template in list_template:
#         res = cv2.matchTemplate(wave_image_gray, corona_template, cv2.TM_CCOEFF_NORMED)
#         loc = np.where(res >= threshold)

#         for pt in zip(*loc[::-1]):
#             ans.append([pt, (pt[0] + width, pt[1] + height)])
#     return ans

def base64_to_image(base64_data):
    encoded_data = base64_data.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)

    return img

async def play_game(websocket, path):
    print('Corona Killer is ready to play!')
    catchings = []
    last_round_id = ''
    wave_count = 0
    
    while True:

        ### receive a socket message (wave)
        try:
            data = await websocket.recv()
        except Exception as e:
            print('Error: ' + e)
            break

        json_data = json.loads(data)

        ### check if starting a new round
        if json_data["roundId"] != last_round_id:
            print(f'> Catching corona for round {json_data["roundId"]}...')
            last_round_id = json_data["roundId"]

        ### catch corona in a wave image
        wave_image = base64_to_image(json_data['base64Image'])
        results = catch_corona(wave_image)

        ### save result image file for debugging purpose
        for result in results:
            cv2.rectangle(wave_image, result[0], result[1], (0, 0, 255), 2)
        
        waves_dir = f'waves/{last_round_id}/'
        if not os.path.exists(waves_dir):
            os.makedirs(waves_dir)
            
        cv2.imwrite(os.path.join(waves_dir, f'{json_data["waveId"]}.jpg'), wave_image)

        print(f'>>> Wave #{wave_count:03d}: {json_data["waveId"]}')
        wave_count = wave_count + 1

        ### store catching positions in the list
        catchings.append({
            "positions": [
                {"x": (result[0][0] + result[1][0]) / 2, "y": (result[0][1] + result[1][1]) / 2} for result in results
            ],
            "waveId": json_data["waveId"]
        })

        ### send result to websocket if it is the last wave
        if json_data["isLastWave"]:
            round_id = json_data["roundId"]
            print(f'> Submitting result for round {round_id}...')

            json_result = {
                "roundId": round_id,
                "catchings": catchings,
            }

            await websocket.send(json.dumps(json_result))
            print('> Submitted.')

            catchings = []
            wave_count = 0


start_server = websockets.serve(play_game, "localhost", 8765, max_size=100000000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
