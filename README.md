# 📐 Leveling Adjustment - Least Squares in Surveying

This repository provides an implementation of **network leveling adjustment** using the **Least Squares Adjustment (LSA)** method, a fundamental technique in **geodetic surveying**.

---

## 📘 Description

In surveying, leveling networks are used to compute the elevation of unknown points based on observed height differences between benchmarks. Due to unavoidable measurement errors, **least squares adjustment** is applied to determine the most probable values for unknown elevations.

This project includes both **Python** and **MATLAB** implementations to:

- Load input data (observations and point indices)
- Construct the design matrix `A` and adjusted observation vector `L₀`
- Estimate unknown heights `X̂`
- Visualize:
  - Residual vector `V`
  - Variance-Covariance Matrix of unknowns `Q`

---

## 📁 File Structure

Leveling-Adjustment/
<pre> Leveling-Adjustment/ ├── Python/ │ ├── proj.py # Python implementation │ ├── y.xlsx # Observation vector │ ├── X.xlsx # x coordinates matrix │ ├── Sind.xlsx # Start point indices │ ├── Eind.xlsx # End point indices │ ├── MATLAB/ │ ├── prj2.m # MATLAB implementation │ ├── data02.mat # Contains y, X, Sind, Eind │ ├── README.md # Project documentation </pre>


---

## 🧠 Mathematical Model

The functional model is:

L = A·X̂ + V

Where:

- `L`: Adjusted observation vector
- `A`: Design matrix
- `X̂`: Vector of unknown elevations
- `V`: Residual vector

The least squares solution:

X̂ = (Aᵀ·W·A)⁻¹ · Aᵀ·W·L₀

Where:

- `W`: Weight matrix (diagonal, based on standard deviation)
- `L₀`: Reduced observation vector based on known control point(s)

---

## ⚙️ How to Run

### ▶️ Python

1. Install dependencies:
   ```bash
   pip install numpy pandas matplotlib
2. Ensure the following Excel files are in the same folder:
y.xlsx, X.xlsx, Sind.xlsx, Eind.xlsx

Run the script:

python proj.py

▶️ MATLAB

Open proj2.m in MATLAB.

Ensure data02.mat is in the same folder.

Run the script.

📊 Output

✅ Estimated elevations of unknown points X̂

✅ Residual vector plot V

✅ Variance-Covariance Matrix plot Q

These help evaluate the quality of measurements and the strength of the network.

📍 Applications

Engineering leveling projects

Geodetic network adjustment

Control point elevation estimation

Integration with GNSS heighting

🤝 Contributing

Feel free to fork the repository, improve the code, or extend it to:

Free networks

Robust adjustment

3D geodetic networks

Pull requests are welcome!

📌 Citation & Usage

If you use this project or parts of its code in your work, please cite the source as follows:

"This project was developed by Mehrshad Hekmatara as part of a study on leveling adjustment using least squares in surveying. Source available at: https://github.com/MehrshadHekmatara/Leveling-Adjustment"

✅ Usage with proper credit is allowed for educational and academic purposes.

👤 Author

Mehrshad Hekmatara

Surveying Engineering, University of Tehran

GitHub: https://github.com/MehrshadHekmatara

Email : hekmataramehrshad532@gmail.com
