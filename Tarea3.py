#Alejandro Restrepo Giraldo CC: 1001389709

from MasaResorte import OsciladorAmortiguado
from MasaResorte import Oscilador


# Se crean las gráficas para el oscilador con condiciones iniciales x_0 = 1.0 y v_0 = -2.0  
sys = Oscilador(1.0,-2.0)
sys.Xvst()
sys.PhaseSpace()


# Se crean las gráficas para el oscilador con condiciones iniciales x_0 = 2.0 y v_0 = -2.0  
sys = OsciladorAmortiguado(2.0,-2.0)
sys.Xvst()
sys.PhaseSpace()
