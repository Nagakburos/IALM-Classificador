from taipy.gui import Gui
from tensorflow.keras import models
from PIL import Image
import numpy as np

class_names = {
    0: 'Avião',
    1: 'Automovel',
    2: 'Passaro',
    3: 'Gato',
    4: 'Veado',
    5: 'Cachorro',
    6: 'Sapo',
    7: 'Cavalo',
    8: 'Ovelha',
    9: 'Caminhão',
}

model = models.load_model("baseline.keras")

def predict_image(model, path_to_img):
    img = Image.open(path_to_img)
    img = img.convert("RGB")
    img = img.resize((32,32))
    data = np.asarray(img)
    data = data /255
    probs = model.predict(np.array([data])[:1])

    top_prob = probs.max()
    top_pred = class_names[np.argmax(probs)]

    return top_prob, top_pred


content = ""
img_path = "placeholder_image.png" ##adiciona Logo
prob = 0
pred = ""

index = """ 
<|text-center|
<|{"logo.png"}|image|width=25vw|>

<|{content}|file_selector|extensions=.png|>
Selecione uma imagem do seu armazenamento

<|{pred}|>

<|{img_path}|image|>

<|Minha Confiança {prob}|indicator|value={prob}|min=0|max=100|width=25vw|>

>
"""


def on_change(state, var_name, var_val):
    if var_name == "content":
        top_prob, top_pred = predict_image(model, var_val)
        state.prob = round(top_prob * 100)
        state.pred =  "isso é um(a) " + top_pred
        state.img_path = var_val


app = Gui (page=index)

if __name__=="__main__":
    app.run(use_reoader=True)