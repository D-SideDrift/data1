import pandas as pd
from flask import Flask, render_template, jsonify, redirect, request
import json

# Flask constructor takes the name of
app = Flask(__name__)

# main driver function
if __name__ == '__main__':
    app.run()

    def to_dict(self):
        return {
            'restaurant': self.restaurant,
            'items': self.items,
            'calories': self.question_id
        }
