from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import numpy as np
from typing import List
import matplotlib
import matplotlib.pyplot as plt
import torch
import density_estimation
import json

matplotlib.use('Agg')  # Usar backend no interactivo
app = FastAPI()

# Definir el modelo para el vector
class VectorF(BaseModel):
    vector: List[float]
    
@app.post("/density-estimation")
def calculo(dataSize: int, bandwidth: float):
    output_file = 'density-estimation.png'
    data = torch.randn(dataSize, 2)  # n puntos en 2D
    #bandwidth = 0.3

    # Calcular densidades
    densities = density_estimation.density_estimation(data, bandwidth)

    # Definir umbral para anomalías (por ejemplo, los puntos con menor densidad)
    threshold = np.percentile(densities, 10)
    anomalies = data[np.array(densities) < threshold]

    # Graficar los datos y resaltar anomalías
    plt.scatter(data[:, 0], data[:, 1], c='blue', label="Normal")
    plt.scatter(anomalies[:, 0], anomalies[:, 1], c='red', label="Anomalías")
    plt.legend()
    plt.title("Detección de Anomalías con Density Estimation")
    #plt.show()
    plt.savefig(output_file)
    plt.close()
    
    j1 = {
        "Grafica": output_file
    }
    jj = json.dumps(str(j1))

    return jj

@app.get("/density-estimation-graph")
def getGraph(output_file: str):
    return FileResponse(output_file, media_type="image/png", filename=output_file)