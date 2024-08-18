---
hide:
  - navigation
  - toc
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TensorFlow</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
        }
        .navbar {
            background-color: #f57c00;
            padding: 1rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .navbar a {
            color: white;
            text-decoration: none;
            margin-left: 1rem;
        }
        .navbar .brand {
            display: flex;
            align-items: center;
        }
        .navbar .brand img {
            height: 30px;
            margin-right: 10px;
        }
        .main-content {
            padding: 2rem;
            text-align: center;
        }
        .main-content h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        .main-content p {
            font-size: 1.2rem;
            color: #555;
        }
        .cta-button {
            background-color: #f57c00;
            color: white;
            padding: 0.8rem 2rem;
            border: none;
            border-radius: 5px;
            font-size: 1.1rem;
            cursor: pointer;
        }
        .tutorials {
            margin-top: 3rem;
            background-color: white;
            padding: 2rem;
            border-radius: 10px;
            display: inline-block;
            text-align: left;
        }
        .code-snippet {
            background-color: #f5f5f5;
            padding: 1rem;
            border-radius: 5px;
            font-family: 'Courier New', Courier, monospace;
            margin-top: 2rem;
            text-align: left;
        }
    </style>
</head>
<body>
    <div class="navbar">
        <div class="brand">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a4/TensorFlowLogo.svg" alt="TensorFlow Logo">
            <span>TensorFlow</span>
        </div>
        <div>
            <a href="#">Install</a>
            <a href="#">Learn</a>
            <a href="#">API</a>
            <a href="#">Ecosystem</a>
            <a href="#">Community</a>
            <a href="#">Why TensorFlow</a>
            <a href="#">GitHub</a>
            <a href="#">Sign In</a>
        </div>
    </div>

    <div class="main-content">
        <h1>An end-to-end platform for machine learning</h1>
        <button class="cta-button">Install TensorFlow</button>
        <div class="tutorials">
            <h2>Get started with TensorFlow</h2>
            <p>TensorFlow makes it easy to create ML models that can run in any environment. Learn how to use the intuitive APIs through interactive code samples.</p>
            <button class="cta-button">View tutorials</button>
        </div>
        <div class="code-snippet">
            <pre>
import tensorflow as tf
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])
            </pre>
        </div>
    </div>
</body>
</html>