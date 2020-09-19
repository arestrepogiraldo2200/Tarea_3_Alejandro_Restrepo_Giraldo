#Alejandro Restrepo Giraldo CC: 1001389709

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


#  ----------------------------------------------------------------------------------------------------------------------------

class Oscilador():

   # Constructor
   def __init__(self, x_0, v_0):
      self.x_0 = x_0
      self.v_0 = v_0



   # Función de graficación de X(t)
   def Xvst(self):

      # Valores de masa, constante del resorte e intervalo de tiempo
      masa = [1.0, 2.0, 3.0]
      kres = [1.0, 2.0, 3.0] 
      t = np.linspace(0,30,3000)

      # figura y ejes
      fig2, ax = plt.subplots(figsize = (15, 15))

      # Gráfica de todas las soluciones en una sola gráfica
      for j in masa:
         for k in kres:
            if j != k or (j == 1 and k == 1 ):
               # Frecuencia angular omega
               w = np.sqrt(k/j)
               # Solución analítica
               sol = self.x_0*np.cos(w*t) + (self.v_0/w)*np.sin(w*t)
               # Gráfica
               ax.plot(t, sol)
               ax.set(title = "Posición en el tiempo", xlabel = "t [s]", ylabel = "X(t) [m]" )
               plt.legend(['k = 1 \n m = 1 ', 'k = 2 \n m = 1 ', 'k = 3 \n m = 1 ', 'k = 1 \n m = 2 ', 'k = 3 \n m = 2 ', 'k = 1 \n m = 3 ', 'k = 2 \n m = 3 '])
 
      # Se guarda la figura
      plt.savefig("Xvst_1plot.png")
      plt.show() 



      # Gráfica de todas las soluciones cada una en una gráfica aparte
      fig1, (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = plt.subplots(7, 1, figsize = (20, 10))

      # Contador de los ejes
      i = 1     
      
      # Gráfica
      for j in masa:
         for k in kres:
            if j != k or (j == 1 and k == 1 ):
               # Frecuencia angular omega
               w = np.sqrt(k/j)
               # Solución analítica
               sol = self.x_0*np.cos(w*t) + (self.v_0/w)*np.sin(w*t)
               # Gráficas y formato
               eval('ax'+str(i)).plot(t, sol)
               ax1.set(title = "Posición en el tiempo")
               ax7.set(xlabel = "t [s]")
               ax4.set(ylabel = "X(t) [m]")
               eval('ax'+str(i)).text(29, -1, "k = " + str(k) + " \nm = " + str(j) )
               i += 1

      # Se guarda la figura
      plt.savefig("Xvst_severalplot.png")
      plt.show() 
 

   # Función de graficación del espacio de fase
   def PhaseSpace(self):

      # Valores de masa, constante del resorte e intervalo de tiempo
      masa = [1.0, 2.0, 3.0]
      kres = [1.0, 2.0, 3.0] 
      t = np.linspace(0,30,30000)

      # figura y ejes
      fig, ax = plt.subplots( figsize = (15, 15))
  
      # Gráfica
      for j in masa:
         for k in kres:
            if j != k or (j == 1 and k == 1 ):
               # Frecuencia angular omega
               w = np.sqrt(k/j)
               # Posición y momento (para este sistema P = mv = m dx/dt)
               X = self.x_0*np.cos(w*t) + (self.v_0/w)*np.sin(w*t)
               P = -self.x_0*j*w*np.sin(w*t) + self.v_0*j*np.cos(w*t)
               # Gráfica y formato
               ax.plot(X, P)
               ax.set(title = "Espacio de fase", xlabel = "x(t) [m]", ylabel = "p(t) [kg m/s]")
               plt.legend(['k = 1' +'\n' +'m = 1 ', 'k = 2 \n m = 1 ', 'k = 3 \n m = 1 ', 'k = 1 \n m = 2 ', 'k = 3 \n m = 2 ', 'k = 1 \n m = 3 ', 'k = 2 \n m = 3 '])

      # Se guarda la figura
      plt.savefig("PhaseSpace.png")         
      plt.show() 


#  ------------------------------------------------------------------------------------------------------------------------




class OsciladorAmortiguado():

   # Constructor
   def __init__(self, x_0, v_0):
      self.x_0 = x_0
      self.v_0 = v_0


   # Función de graficación de X(t)
   def Xvst(self):

      # Valores de masa, constante del resorte y constante de amortiguamiento (masa, constante del resorte, coeficiente de fricción)
      param = [[1,1,1],[1,3,2.3],[10,3,2],[10, 12, 2.3],[15,3,3]]
      t = np.linspace(0,30,2000)
      # Condición inicial
      X_0 = [self.x_0, self.v_0]

      # Función linealizada del sistema
      def Sistema(y,t,m,k,b):
         return [y[1], -k/m*y[0] - b/m*y[1]]


      # figura y ejes
      fig2, ax = plt.subplots(figsize = (15, 15))

      # Gráfica de todas las soluciones en una sola gráfica
      for j in param:
         # Solución numérica
         sol = odeint(Sistema, X_0, t, args=(j[0], j[1], j[2]))
         # Gráfica
         ax.plot(t, sol[:,0])
         ax.set(title = "Posición en el tiempo", xlabel = "t [s]", ylabel = "X(t) [m]" )
         plt.legend(['m = 1 \n k = 1 \n b = 1', 'm = 1 \n k = 3 \n b = 2.3', 'm = 10 \n k = 3 \n b = 2', 'm = 10 \n k = 12 \n b = 2.3', 'm = 15 \n k = 3 \n b = 3'])
 
      # Se guarda la figura
      plt.savefig("XvstAmort_1plot.png")
      plt.show() 





      # Gráfica de todas las soluciones cada una en una gráfica aparte
      fig1, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, 1, figsize = (20, 10))

      # Contador de los ejes
      i = 1     
      
      # Gráfica
      for j in param:
         # Solución numérica
         sol = odeint(Sistema, X_0, t, args=(j[0], j[1], j[2]))
         # Gráficas y formato
         eval('ax'+str(i)).plot(t, sol[:,0])
         ax1.set(title = "Posición en el tiempo")
         ax5.set(xlabel = "t [s]")
         ax2.set(ylabel = "X(t) [m]")
         eval('ax'+str(i)).text(29, 0, "m = " + str(j[0]) + " \nk = " + str(j[1])+ "\nb = " + str(j[2]) )
         i += 1

      # Se guarda la figura
      plt.savefig("XvstAmort_severalplot.png")
      plt.show() 
 

   # Función de graficación del espacio de fase
   def PhaseSpace(self):

     # Valores de masa, constante del resorte y constante de amortiguamiento (masa, constante del resorte, coeficiente de fricción)
      param = [[1,1,1],[1,3,2.3],[10,3,2],[10, 12, 2.3],[15,3,3]]
      t = np.linspace(0,30,2000)
      # Condición inicial
      X_0 = [self.x_0, self.v_0]

      # Función linealizada del sistema
      def Sistema(y,t,m,k,b):
         return [y[1], -k/m*y[0] - b/m*y[1]]


      # figura y ejes
      fig, ax = plt.subplots( figsize = (15, 15))
  
      # Gráfica
      for j in param:
         # Solución numérica
         sol = odeint(Sistema, X_0, t, args=(j[0], j[1], j[2]))
         ax.plot(sol[:,0], j[0]*sol[:,1])
         ax.set(title = "Espacio de fase", xlabel = "x(t) [m]", ylabel = "p(t) [kg m/s]")
         plt.legend(['m = 1 \n k = 1 \n b = 1', 'm = 1 \n k = 3 \n b = 2.3', 'm = 10 \n k = 3 \n b = 2', 'm = 10 \n k = 12 \n b = 2.3', 'm = 15 \n k = 3 \n b = 3'])

      # Se guarda la figura
      plt.savefig("PhaseSpaceAmort.png")         
      plt.show() 


#  ---------------------------------------------------------------------------------------------------------------





sys = OsciladorAmortiguado(1.0,-2.0)
sys.Xvst()
sys.PhaseSpace()

sys = Oscilador(1.0,-2.0)
sys.Xvst()
sys.PhaseSpace()
