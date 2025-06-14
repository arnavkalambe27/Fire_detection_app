{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4d7dec1a-5e83-4f4b-b5b5-e5bf9077a45f",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-06-14 12:30:00.236 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run /opt/anaconda3/lib/python3.12/site-packages/ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import numpy as np\n",
    "from tensorflow.keras.models import load_model\n",
    "from PIL import Image, ImageOps\n",
    "\n",
    "# Set up app config\n",
    "st.set_page_config(page_title=\"Fire Detection from Satellite\", layout=\"centered\")\n",
    "\n",
    "st.title(\"Fire Detection from Satellite Images\")\n",
    "st.write(\"Upload a satellite image to detect presence of Fire or Not Fire\")\n",
    "\n",
    "# Load model (cache it)\n",
    "@st.cache_resource\n",
    "def load_fire_model():\n",
    "    model = load_model(\"fire_detection_model.h5\")\n",
    "    return model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aa0e6348-53a3-475a-a4d4-6f12150a3289",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
