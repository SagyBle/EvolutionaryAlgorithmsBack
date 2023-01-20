# import Graph
import json

import Data
import EvolutionaryColores

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def cala_evo(data):
    data = json.loads(data)
    k = data.pop(0)
    print("k:", k)
    Data.Data.NUM_OF_COLORS = int(k)
    num_of_students = 0
    edges_list = []
    kids_list = []
    for kid in data:
        u = int(kid['kidID'])
        if u not in kids_list: kids_list.append(u)
        for enemy in kid['kidEnemies']:
            v = int(enemy)
            if v not in kids_list: kids_list.append(v)
            if (u, v) not in edges_list:
                edges_list.append((u, v))

    print(edges_list)
    print(sorted(kids_list))
    Data.Data.NUM_OF_VERTICES = len(kids_list)
    print("Data.Data.NUM_OF_VERTICES: ", Data.Data.NUM_OF_VERTICES)
    Data.Data.EDJES_LIST = edges_list
    print("Data.Data.NUM_OF_COLORS", Data.Data.NUM_OF_COLORS)

    Data.Data.END_CALC = False
    EvolutionaryColores.algo.evolve()

    print("end and waiting to send data")
    return Data.Data.colors


if __name__ == '__main__':
    app = FastAPI()

    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


    @app.get("/")
    async def root():
        return {"body": "Hello World"}


    @app.get("/{data_json}")
    async def root(data_json):
        cala_evo(data_json)
        while not Data.Data.END_CALC:
            # waiting to calc_evo to change END_CALC to true
            pass

        num_of_colors = Data.Data.NUM_OF_COLORS
        teams = []
        colors = Data.Data.colors
        for i in range(0, num_of_colors):
            teams.append([])
        for i in range(0, len(Data.Data.colors)):
            teams[colors[i]].append(i)

        print(teams)
        return {'colors': Data.Data.colors, 'fitness': Data.Data.fitness, 'teams':teams}




    uvicorn.run(app, host="0.0.0.0", port=8000)



