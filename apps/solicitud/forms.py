from django import forms
from apps.simulacion.models import Simulador


velocidades= (
		('1',0.15),
		('2',0.30),
		('3',0.45),
		('4',0.60),
		('5',0.75),
		('6',0.90),
		('7',1),
	)

pisos= (
		('1',1),
		('2',2),
		('3',3),
		('4',4),
		('5',5),
		('6',6),
		('7',7),
		('8',8),
		('9',9),
		('10',10),
	)
expanciones= (
		('1',1),
		('2',2),
		('3',3),		
	)


class ModificacionForm(forms.ModelForm):

	class Meta:
		model = Simulador

		fields = [
			'numero_Cables',
			'carga_Nominal',
			'recorrido_Cabina',
			'recorido_Superior_Piston',
			'cantidad_Pistones',
			'cantidad_Cilindros',
			'numero_Expanciones',
			'velocidad_Cabina',
			'diametro_Cable',
			'peso_Ascensor',
			'diametro_Piston',
			'masa_Embolo',			
			'usuario',
		
		]

		labels = {
			'numero_Cables': 'Cantidad de cables',
			'carga_Nominal': 'Carga nominal',
			'recorrido_Cabina': 'Recorrido de la cabina',
			'recorido_Superior_Piston': 'Recorrido superior del piston',
			'cantidad_Pistones': 'Cantidad de pistones',
			'cantidad_Cilindros': 'Cantidad de cilindros',
			'numero_Expanciones': 'Cantidad de expanciones',
			'velocidad_Cabina': 'Velocidad de la cabina',
			'diametro_Cable': 'Diametro del cable',
			'peso_Ascensor': 'Peso del ascensor',
			'diametro_Piston': 'Diametro del piston',
			'masa_Embolo': 'Masa del embolo',
			'usuario': 'Usuario',	
		}

		# forms.select porque es una llave foranea

		widgets = {
			'numero_Cables': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"cables"}),
			'carga_Nominal': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"peso"}),
			'recorrido_Cabina': forms.Select(attrs={'class': 'form-control'},choices=pisos),
			'recorido_Superior_Piston': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"recorrido piston"}),
			'cantidad_Pistones': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Pistones"}),
			'cantidad_Cilindros': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"cilindros"}),
			'numero_Expanciones': forms.Select(attrs={'class': 'form-control'},choices=expanciones),
			'diametro_Cable': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"diametro del cable"}),
			'velocidad_Cabina': forms.Select(attrs={'class': 'form-control'},choices= velocidades),
			'peso_Ascensor': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"peso"}),
			'diametro_Piston': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"diametro"}),
			'masa_Embolo': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"masa embolo"}),
			'usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Ingrese el id de la simulacion"}),

			
		}
