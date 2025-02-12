#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <torch/torch.h>
#include <vector>

namespace py = pybind11;

// Función para calcular la densidad de cada punto usando KDE con una gaussiana
std::vector<double> density_estimation(torch::Tensor data, double bandwidth) {
    int n = data.size(0);
    std::vector<double> densities(n, 0.0);
    
    for (int i = 0; i < n; i++) {
        double sum = 0.0;
        for (int j = 0; j < n; j++) {
            double dist = torch::norm(data[i] - data[j]).item<double>();
            sum += exp(-0.5 * (dist * dist) / (bandwidth * bandwidth));
        }
        densities[i] = sum / (n * sqrt(2 * M_PI) * bandwidth);
    }
    return densities;
}

PYBIND11_MODULE(density_estimation, m) {
    m.def("density_estimation", &density_estimation, "Density estimation using Gaussian Kernel", 
          py::arg("data"), py::arg("bandwidth"));
}
