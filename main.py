# from flask import Flask, render_template, request
# import pickle
# # Create an object of the class Flask
# app = Flask(__name__)
# model=pickle.load(open('model.pkl','rb'))

# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/predict',methods=['GET','POST'])
# def predict():
#     prediction=model.predict([[request.form.get('temperature')]])
#     output=round(prediction[0],2)
#     print(output)
#     print(prediction)
#     return render_template('index.html',prediction_text=f"Total revenue generated will bw: {output}/-")



# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request
import pickle

# Create an object of the class Flask
app = Flask(__name__)

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input from the form
    try:
        input_value = float(request.form.get('temperature'))
        # Make prediction
        prediction = model.predict([[input_value]])
        prediction_text = f'Prediction: {prediction[0]}'
    except ValueError:
        prediction_text = 'Invalid input. Please enter a numeric value.'
    except Exception as e:
        prediction_text = f'Error: {str(e)}'
    
    # Render result on the template
    return render_template('index.html', prediction_text=prediction_text)

# if __name__ == '__main__':
#     app.run(debug=True)

