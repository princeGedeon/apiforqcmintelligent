import pandas as pd

from utils.parsers import parse_questions


def generate_qcm_with_model(ludwig_model,lyric,default_format=False):
  data=pd.DataFrame([
      {
            "instruction": "Donne moi 3 QCM exactement",

            "input":lyric  },


])

  predictions, _ = ludwig_model.predict(dataset=data)
  return parse_questions(predictions['output_response'][0][0]) if not default_format else predictions['output_response'][0][0]