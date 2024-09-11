% Definir la matriz de coeficientes
A = [0.52, 0.20, 0.25;
     0.30, 0.50, 0.20;
     0.18, 0.30, 0.55];

% Definir el vector de resultados
b = [4800; 5810; 5690];

% Resolver el sistema de ecuaciones
x = A\b;

% Mostrar el resultado
disp('Los metros cúbicos que se deben extraer de cada cantera son:');
disp(x);

