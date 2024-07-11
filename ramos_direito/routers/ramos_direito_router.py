import joblib
from fastapi import APIRouter, HTTPException
import pandas as pd

router: APIRouter = APIRouter(prefix="/busca-peca")

df = pd.read_csv("dados/tags_transformadas.csv")

model_tags = joblib.load('LR_pipeline_cadeia.joblib')

tags_labels = ['DIREITO ADMINISTRATIVO E OUTRAS MATÉRIAS DE DIREITO PÚBLICO',
               'DIREITO PROCESSUAL CIVIL E DO TRABALHO',
               'DIREITO TRIBUTÁRIO',
               'DIREITO CIVIL',
               'DIREITO PROCESSUAL PENAL']


@router.get("/{index}")
def busca_texto(index: int):
    try:
        texto = df['texto_bruto'][index]
        ramo_r = df['ramo_direito'][index]
        lista_prev = model_tags.predict([texto]).toarray()
        dados_bs = {'ramo': tags_labels,
                    'valores': lista_prev[0]
                    }
        df_teste = pd.DataFrame.from_dict(dados_bs)
        previsao = df_teste[df_teste['valores'] == 1.0]['ramo'].tolist()

        return {
            'previsao': previsao,
            'ramo_real': ramo_r,
            'texto': texto
        }
    except IndexError:
        raise HTTPException(status_code=404, detail="Não existe nenhuma peça com este id")
