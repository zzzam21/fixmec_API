from experta import KnowledgeEngine, Fact, Rule

class Sintoma(Fact):
    """Representa un síntoma reportado por el usuario."""

class DiagnosticoMoto(KnowledgeEngine):
    
    def __init__(self):
        super().__init__()
        self.resultado = None
    
    @Rule(Sintoma(diagnosis="inicial"))
    def inicio(self):
        self.declare(Sintoma(
            key="diagnostico_inicial",
            pregunta="¿Cuál es el sistema que presenta fallas?",
            opciones=['Freno', 'Motor', 'Suspensión']
        ))
    
    # ────────────────────────────────────────────── 
    # RAMA: SISTEMA DE FRENOS
    # ──────────────────────────────────────────────
    @Rule(Sintoma(diagnostico_inicial='Freno'))
    def rama_freno(self):
        self.declare(Sintoma(
            key="tipo_freno",
            pregunta="¿Qué tipo de freno tiene la motocicleta?",
            opciones=['Disco', 'Tambor']
        ))
    
    # ──────────────────────────────────────────────
    # RAMA: FRENOS DE DISCO
    # ──────────────────────────────────────────────
    @Rule(Sintoma(tipo_freno='Disco'))
    def diagnosticar_freno_disco(self):
        self.declare(Sintoma(
            key="sintoma_freno",
            pregunta="¿El freno de disco presenta alguno de los siguientes síntomas?",
            opciones=['Poca presion al frenar', 'Ruidos al frenar', 'Vibraciones al frenar']
        ))
    
    # ───────────────────────────────────────────────
    # RAMA: RUIDOS AL FRENAR
    # ───────────────────────────────────────────────
    @Rule(Sintoma(sintoma_freno='Ruidos al frenar'))
    def preguntar_tipo_ruido(self):
        self.declare(Sintoma(
            key="sonido",
            pregunta="¿Qué tipo de ruido presenta el freno?",
            opciones=["Chillido agudo", "Ruido metálico"]
        ))

    @Rule(Sintoma(sonido='Chillido agudo'))
    def pastillas_cristalizadas(self):
        self.declare(Sintoma(
            diagnostico="Probables pastillas cristalizadas. Recomendación: lijar o reemplazar pastillas."
        ))


    @Rule(Sintoma(sonido='Ruido metálico'))
    def pastillas_gastadas(self):
        self.declare(Sintoma(
            diagnostico="Posible desgaste excesivo de pastillas o contacto metal con metal. Cambiar pastillas urgentemente."
        ))


    # ───────────────────────────────────────────────
    # RAMA: VIBRACIONES AL FRENAR
    # ───────────────────────────────────────────────
    @Rule(Sintoma(sintoma_freno='Vibraciones al frenar'))
    def preguntar_frecuencia_vibracion(self):
        self.declare(Sintoma(
            key="vibracion",
            pregunta="¿La vibración aumenta al frenar a alta velocidad?",
            opciones=["Si", "No"]
        ))
    
    @Rule(Sintoma(vibracion='Si'))
    def disco_deformado(self):
        self.declare(Sintoma(
            diagnostico="Probable disco de freno deformado. Recomendar rectificación o reemplazo."
        ))


    @Rule(Sintoma(vibracion='No'))
    def soporte_flotante_suelto(self):
        self.declare(Sintoma(
            diagnostico="Posible pinza floja o buje desgastado. Revisar pernos, rodamientos y anclajes."
        ))

    # ───────────────────────────────────────────────
    # RAMA POCA PRESIÓN
    # ───────────────────────────────────────────────
    @Rule(Sintoma(sintoma_freno='Poca presion al frenar'))
    def preguntar_nivel_liquido(self):
        self.declare(Sintoma(
            key="nivel",
            pregunta="¿Cuál es el nivel del líquido de frenos?",
            opciones=["Bajo", "Alto"]
        ))

    @Rule(Sintoma(nivel='Bajo'))
    def fuga_sistema_hidraulico(self):
        self.declare(Sintoma(
            key="cambio_liquido",
            pregunta="¿Se realizó cambio de líquido de frenos recientemente?",
            opciones=["Si", "No"]
        ))

    @Rule(Sintoma(cambio_liquido='No'))
    def diagnostico_fuga(self):
        self.declare(Sintoma(
            diagnostico="Nivel bajo: posible fuga. Inspeccionar líneas, bomba y cáliper."
        ))

    @Rule(Sintoma(cambio_liquido='Si'))
    def revisar_fugas(self):
        self.declare(Sintoma(
            diagnostico="Revisar sistema hidráulico por posibles fugas después del cambio."
        ))

    @Rule(Sintoma(nivel='Alto'))
    def preguntar_tacto(self):
        self.declare(Sintoma(
            key="tacto",
            pregunta="¿Cuál es el tacto de la manigueta?",
            opciones=["Esponjosa", "Firme"]
        ))

    @Rule(Sintoma(tacto='Esponjosa'))
    def aire_en_sistema(self):
        self.declare(Sintoma(
            diagnostico="Presencia de aire en el sistema. Recomendación: purgar frenos."
        ))

    @Rule(Sintoma(tacto='Firme'))
    def cilindro_defectuoso(self):
        self.declare(Sintoma(
            diagnostico="Probable cilindro maestro defectuoso."
        ))
    # ───────────────────────────────────────────────
    # FIN RAMA FRENOS DE DISCO
    # ───────────────────────────────────────────────
    
    # ──────────────────────────────────────────────
    # RAMA: FRENOS DE TAMBOR
    # ───────────────────────────────────────────

    @Rule(Sintoma(tipo_freno='Tambor'))
    def inicio_tambor(self):
        self.declare(Sintoma(
            key="sintoma_tambor",
            pregunta="¿Qué síntoma presenta el freno de tambor?",
            opciones=[
                "Poca frenada",
                "Ruidos al frenar",
                "Vibraciones",
                "Pedal hundido",
                "Frena demasiado o se traba"
            ]
        ))


    # ───────────────────────────────────────────────
    # RAMA — POCA FRENADA
    # ───────────────────────────────────────────────

    @Rule(Sintoma(sintoma_tambor='Poca frenada'))
    def preguntar_ajuste(self):
        self.declare(Sintoma(
            key="ajuste",
            pregunta="¿El freno fue ajustado recientemente?",
            opciones=["Sí", "No"]
        ))


    @Rule(Sintoma(ajuste='No'))
    def recomendar_ajuste(self):
        self.declare(Sintoma(
            diagnostico=(
                "Desajuste del sistema de freno. Ajustar varilla, leva y pedal.\n"
                "Recomendación: regular tensión del freno y revisar resortes."
            )
        ))


    @Rule(Sintoma(ajuste='Sí'))
    def preguntar_desgaste(self):
        self.declare(Sintoma(
            key="desgaste_zapatas",
            pregunta="¿Las zapatas presentan desgaste visible?",
            opciones=["Sí", "No", "No se revisaron"]
        ))


    @Rule(Sintoma(desgaste_zapatas='Sí'))
    def diagnostico_zapatas_gastadas(self):
        self.declare(Sintoma(
            diagnostico=(
                "Zapatas desgastadas, reducen la fuerza de frenado.\n"
                "Recomendación: reemplazar zapatas y revisar diámetro del tambor."
            )
        ))


    @Rule(Sintoma(desgaste_zapatas='No'))
    def preguntar_contaminacion(self):
        self.declare(Sintoma(
            key="contaminacion",
            pregunta="¿Las zapatas o el tambor tienen grasa, aceite o líquido?",
            opciones=["Sí", "No"]
        ))


    @Rule(Sintoma(contaminacion='Sí'))
    def diagnostico_contaminacion(self):
        self.declare(Sintoma(
            diagnostico=(
                "Contaminación del material de fricción.\n"
                "Recomendación: desengrasar tambor y reemplazar zapatas."
            )
        ))


    @Rule(Sintoma(contaminacion='No'))
    def revisar_leva(self):
        self.declare(Sintoma(
            diagnostico=(
                "Leva de expansión desgastada o con poca apertura.\n"
                "Recomendación: revisar mecanismo interno del tambor."
            )
        ))

    
    @Rule(Sintoma(sintoma_tambor='Frena demasiado o se traba'))
    def preguntar_trabado_inicial(self):
        self.declare(Sintoma(
            key="bloqueo_tambor",
            pregunta="¿Cuándo ocurre el bloqueo o exceso de frenado?",
            opciones=[
                "Al inicio del recorrido",
                "Sólo después de usar un rato",
                "Incluso sin presionar el freno"
            ]
        ))


    #  EXCESO DE TENSIÓN DEL CABLE
    @Rule(Sintoma(bloqueo_tambor='Al inicio del recorrido'))
    def exceso_tension(self):
        self.declare(Sintoma(
            diagnostico="El freno está demasiado ajustado o el cable tiene exceso de tensión. "
                        "Ajustar holgura del pedal/manigueta y revisar lubricación del cable."
        ))


    #  DILATACIÓN POR CALENTAMIENTO / ZAPATAS NUEVAS
    @Rule(Sintoma(bloqueo_tambor='Sólo después de usar un rato'))
    def freno_se_traba_caliente(self):
        self.declare(Sintoma(
            diagnostico="El tambor o las zapatas se dilatan con el calor, generando bloqueo. "
                        "Posible mala rectificación, zapatas nuevas sin asentamiento o ajuste excesivo."
        ))


    #  LEVA PEGADA / RESORTE ROTO / ZAPATAS CONTAMINADAS
    @Rule(Sintoma(bloqueo_tambor='Incluso sin presionar el freno'))
    def freno_trabado_constante(self):
        self.declare(Sintoma(
            diagnostico="El freno permanece trabado incluso sin accionar: posible resorte de retorno roto, "
                        "leva pegada, óxido interno o ingreso de aceite al tambor. "
                        "Recomendación: desmontar, limpiar, lubricar y reemplazar componentes dañados."
        ))

    # ───────────────────────────────────────────────
    # RAMA — RUIDOS AL FRENAR
    # ───────────────────────────────────────────────

    @Rule(Sintoma(sintoma_tambor='Ruidos al frenar'))
    def preguntar_tipo_ruido(self):
        self.declare(Sintoma(
            key="ruido_tambor",
            pregunta="¿Qué tipo de ruido produce?",
            opciones=["Chirrido agudo", "Golpeteo seco", "Ruido metálico"]
        ))


    @Rule(Sintoma(ruido_tambor='Chirrido agudo'))
    def preguntar_limpieza(self):
        self.declare(Sintoma(
            key="ultima_limpieza",
            pregunta="¿Hace cuánto se limpió el tambor?",
            opciones=["Menos de 6 meses", "Más de 6 meses", "Nunca"]
        ))


    @Rule(Sintoma(ultima_limpieza='Más de 6 meses') | Sintoma(ultima_limpieza='Nunca'))
    def diagnostico_suciedad(self):
        self.declare(Sintoma(
            diagnostico=(
                "Ruido por acumulación de polvo dentro del tambor.\n"
                "Recomendación: desmontar y limpiar cada 5.000 km."
            )
        ))


    @Rule(Sintoma(ultima_limpieza='Menos de 6 meses'))
    def diagnostico_cristalizacion(self):
        self.declare(Sintoma(
            diagnostico=(
                "Posible cristalización del material de fricción.\n"
                "Recomendación: lijar o reemplazar zapatas."
            )
        ))


    @Rule(Sintoma(ruido_tambor='Golpeteo seco'))
    def diagnostico_pernos_flojos(self):
        self.declare(Sintoma(
            diagnostico=(
                "Golpeteo causado por holgura en componentes internos.\n"
                "Recomendación: revisar pernos, bujes y anclajes del freno."
            )
        ))


    @Rule(Sintoma(ruido_tambor='Ruido metálico'))
    def diagnostico_contacto_metalico(self):
        self.declare(Sintoma(
            diagnostico=(
                "Contacto metal con metal por desgaste total de zapatas.\n"
                "Recomendación: cambiar zapatas urgentemente."
            )
        ))


    # ───────────────────────────────────────────────
    # RAMA — VIBRACIONES
    # ───────────────────────────────────────────────

    @Rule(Sintoma(sintoma_tambor='Vibraciones'))
    def preguntar_ovalado(self):
        self.declare(Sintoma(
            key="ovalado",
            pregunta="¿El tambor presenta desgaste irregular u ovalado?",
            opciones=["Sí", "No", "No se sabe"]
        ))


    @Rule(Sintoma(ovalado='Sí'))
    def diagnostico_tambor_ovalado(self):
        self.declare(Sintoma(
            diagnostico=(
                "Tambor ovalado causa vibración.\n"
                "Recomendación: rectificar si está dentro de tolerancia o reemplazar."
            )
        ))


    @Rule(Sintoma(ovalado='No'))
    def diagnostico_rodamientos(self):
        self.declare(Sintoma(
            diagnostico=(
                "Vibraciones por rodamientos desgastados.\n"
                "Recomendación: revisar y reemplazar rodamientos."
            )
        ))


    # ───────────────────────────────────────────────
    # RAMA — PEDAL HUNDIDO
    # ───────────────────────────────────────────────

    @Rule(Sintoma(sintoma_tambor='Pedal hundido'))
    def preguntar_holgura(self):
        self.declare(Sintoma(
            key="holgura",
            pregunta="¿El pedal tiene demasiada holgura al inicio?",
            opciones=["Sí", "No"]
        ))


    @Rule(Sintoma(holgura='Sí'))
    def diagnostico_holgura(self):
        self.declare(Sintoma(
            diagnostico=(
                "Holgura excesiva en la varilla del freno.\n"
                "Recomendación: ajustar recorrido del pedal."
            )
        ))


    @Rule(Sintoma(holgura='No'))
    def diagnostico_resortes_debilitados(self):
        self.declare(Sintoma(
            diagnostico=(
                "Resortes de retorno fatigados.\n"
                "Recomendación: reemplazar ambos resortes del freno."
            )
        ))

    # ───────────────────────────────────────────────
    # RAMA — FRENO SE TRABA / SE QUEDA PEGADO
    # ───────────────────────────────────────────────

    @Rule(Sintoma(sintoma_tambor='Frena demasiado o se traba'))
    def preguntar_resortes(self):
        self.declare(Sintoma(
            key="resortes",
            pregunta="¿Los resortes del tambor están en buen estado?",
            opciones=["Sí", "No", "No se revisaron"]
        ))


    @Rule(Sintoma(resortes='No'))
    def diagnostico_resortes(self):
        self.declare(Sintoma(
            diagnostico=(
                "Resortes dañados hacen que el freno quede pegado.\n"
                "Recomendación: reemplazar inmediatamente."
            )
        ))


    @Rule(Sintoma(resortes='Sí'))
    def diagnostico_leva_oxido(self):
        self.declare(Sintoma(
            diagnostico=(
                "Leva interna oxidada o sin lubricación.\n"
                "Recomendación: desmontar, limpiar y lubricar."
            )
        ))

    # ──────────────────────────────────────────────
    # DIAGNOSTICOS DE MOTOR
    # ──────────────────────────────────────────────

    @Rule(Sintoma(diagnostico_inicial='Motor'))
    def inicio_motor(self):
        self.declare(Sintoma(
            key="sintoma_motor",
            pregunta="¿Qué síntoma presenta el motor?",
            opciones=[
                "Difícil encendido",
                "Pérdida de potencia",
                "Humo en el escape",
                "Ruidos anormales",
                "Vibraciones excesivas",
                "Sobrecalentamiento" 
            ]
        ))

    # ───────────────────────────────────────────────
    # RAMA — DIFÍCIL ENCENDIDO
    # ───────────────────────────────────────────────

    @Rule(Sintoma(sintoma_motor='Difícil encendido'))
    def preguntar_bateria(self):
        self.declare(Sintoma(
            key="estado_bateria",
            pregunta="¿La batería gira con fuerza al intentar encender?",
            opciones=["Sí", "No"]
        ))


    @Rule(Sintoma(estado_bateria='No'))
    def diagnostico_bateria(self):
        self.declare(Sintoma(
            diagnostico=(
                "Posible batería descargada o defectuosa.\n"
                "Recomendación: medir voltaje (mínimo 12.4V) y revisar bornes."
            )
        ))


    @Rule(Sintoma(estado_bateria='Sí'))
    def preguntar_combustible(self):
        self.declare(Sintoma(
            key="combustible",
            pregunta="¿Hay suficiente combustible en el tanque?",
            opciones=["Sí", "No"]
        ))


    @Rule(Sintoma(combustible='No'))
    def diagnostico_sin_gasolina(self):
        self.declare(Sintoma(
            diagnostico=(
                "Motor no enciende debido a falta de combustible.\n"
                "Recomendación: repostar y purgar línea si es necesario."
            )
        ))


    @Rule(Sintoma(combustible='Sí'))
    def preguntar_bujia(self):
        self.declare(Sintoma(
            key="estado_bujia",
            pregunta="¿La bujía presenta chispa?",
            opciones=["Sí", "No", "No se revisó"]
        ))


    @Rule(Sintoma(estado_bujia='No'))
    def diagnostico_bujia(self):
        self.declare(Sintoma(
            diagnostico=(
                "Falla en el encendido: bujía o bobina defectuosa.\n"
                "Recomendación: limpiar, calibrar o reemplazar."
            )
        ))


    @Rule(Sintoma(estado_bujia='Sí'))
    def diagnostico_carb(self):
        self.declare(Sintoma(
            diagnostico=(
                "Posible mezcla incorrecta o carburador/inyección sucia.\n"
                "Recomendación: limpieza y calibración del sistema de admisión."
            )
        ))


    # ───────────────────────────────────────────────
    # RAMA — PÉRDIDA DE POTENCIA
    # ───────────────────────────────────────────────

    @Rule(Sintoma(sintoma_motor='Pérdida de potencia'))
    def preguntar_aceleracion(self):
        self.declare(Sintoma(
            key="tironeos",
            pregunta="¿La moto tironea o se ahoga al acelerar?",
            opciones=["Sí", "No"]
        ))


    @Rule(Sintoma(tironeos='Sí'))
    def diagnostico_filtro_aire(self):
        self.declare(Sintoma(
            diagnostico=(
                "Posible filtro de aire sucio o entrada de aire restringida.\n"
                "Recomendación: limpiar o reemplazar filtro."
            )
        ))


    @Rule(Sintoma(tironeos='No'))
    def preguntar_compresion(self):
        self.declare(Sintoma(
            key="compresion",
            pregunta="¿Se ha medido la compresión del motor?",
            opciones=["Normal", "Baja"]
        ))


    @Rule(Sintoma(compresion='Baja'))
    def diagnostico_compresion_baja(self):
        self.declare(Sintoma(
            diagnostico=(
                "Compresión baja.\n"
                "Posibles causas:\n"
                "• Desgaste de anillos\n"
                "• Válvulas mal asentadas\n"
                "• Empaque de culata defectuoso\n\n"
                "Recomendación: prueba de fugas y reparación interna."
            )
        ))


    @Rule(Sintoma(compresion='Normal'))
    def diagnostico_combustible(self):
        self.declare(Sintoma(
            diagnostico=(
                "Combustible deficiente o inyector sucio.\n"
                "Recomendación: limpiar sistema de alimentación."
            )
        ))


    # ───────────────────────────────────────────────
    # RAMA — HUMO EN EL ESCAPE
    # ───────────────────────────────────────────────

    @Rule(Sintoma(sintoma_motor='Humo en el escape'))
    def preguntar_color_humo(self):
        self.declare(Sintoma(
            key="color_humo",
            pregunta="¿Qué color tiene el humo del escape?",
            opciones=["Azul", "Negro", "Blanco"]
        ))


    @Rule(Sintoma(color_humo='Azul'))
    def diagnostico_aceite(self):
        self.declare(Sintoma(
            diagnostico=(
                "Quema de aceite en la combustión.\n"
                "Causas típicas:\n"
                "• Anillos desgastados\n"
                "• Guías o retenes de válvulas dañados\n"
                "• Nivel de aceite excesivo\n\n"
                "Recomendación: revisión interna del motor."
            )
        ))


    @Rule(Sintoma(color_humo='Negro'))
    def diagnostico_mezcla_rica(self):
        self.declare(Sintoma(
            diagnostico=(
                "Mezcla demasiado rica.\n"
                "Causas:\n"
                "• Filtro de aire sucio\n"
                "• Chiclés sobredimensionados\n"
                "• Sensor O2 o inyector fallando\n\n"
                "Recomendación: ajustar mezcla aire/combustible."
            )
        ))


    @Rule(Sintoma(color_humo='Blanco'))
    def diagnostico_refrigerante(self):
        self.declare(Sintoma(
            diagnostico=(
                "Posible ingreso de refrigerante al cilindro.\n"
                "Recomendación: revisar empaque de culata."
            )
        ))


    # ───────────────────────────────────────────────
    # RAMA — RUIDOS ANORMALES
    # ───────────────────────────────────────────────

    @Rule(Sintoma(sintoma_motor='Ruidos anormales'))
    def preguntar_tipo_ruido(self):
        self.declare(Sintoma(
            key="tipo_ruido",
            pregunta="¿Qué tipo de ruido presenta el motor?",
            opciones=["Golpeteo metálico", "Cascabeleo", "Zumbido agudo"]
        ))


    @Rule(Sintoma(tipo_ruido='Golpeteo metálico'))
    def diagnostico_biela(self):
        self.declare(Sintoma(
            diagnostico=(
                "Posible desgaste de cojinetes de biela.\n"
                "Recomendación: no circular y revisar fondo de motor."
            )
        ))


    @Rule(Sintoma(tipo_ruido='Cascabeleo'))
    def diagnostico_detonacion(self):
        self.declare(Sintoma(
            diagnostico=(
                "Detonación por mala combustión.\n"
                "Recomendación: usar gasolina adecuada y revisar avance de encendido."
            )
        ))


    @Rule(Sintoma(tipo_ruido='Zumbido agudo'))
    def diagnostico_rodamientos_eje(self):
        self.declare(Sintoma(
            diagnostico=(
                "Rodamientos de cigüeñal o árbol de levas desgastados.\n"
                "Recomendación: inspección interna urgente."
            )
        ))


    # ───────────────────────────────────────────────
    # RAMA — SOBRECALENTAMIENTO
    # ───────────────────────────────────────────────

    @Rule(Sintoma(sintoma_motor='Sobrecalentamiento'))
    def preguntar_refrigerante(self):
        self.declare(Sintoma(
            key="nivel_refrigerante",
            pregunta="¿El nivel de refrigerante está dentro del rango?",
            opciones=["Sí", "No", "No aplica (motor aire)"]
        ))


    @Rule(Sintoma(nivel_refrigerante='No'))
    def diagnostico_fuga_refrigerante(self):
        self.declare(Sintoma(
            diagnostico=(
                "Nivel de refrigerante bajo por fuga.\n"
                "Recomendación: inspeccionar mangueras, radiador y bomba."
            )
        ))


    @Rule(Sintoma(nivel_refrigerante='Sí'))
    def diagnostico_termostato(self):
        self.declare(Sintoma(
            diagnostico=(
                "Posible termostato o ventilador defectuoso.\n"
                "Recomendación: probar funcionamiento del sistema de enfriamiento."
            )
        ))

    
    @Rule(Sintoma(nivel_refrigerante='No aplica (motor aire)'))
    def preguntar_flujo_aire(self):
        self.declare(Sintoma(
            key="flujo_aire",
            pregunta="¿Las aletas del cilindro están limpias y permiten buen flujo de aire?",
            opciones=["Sí", "No", "No estoy seguro"]
        ))

    @Rule(Sintoma(flujo_aire='No'))
    def aletas_obstruidas(self):
        self.declare(Sintoma(
            diagnostico="Aletas de cilindro obstruidas por tierra o grasa. Esto reduce la disipación de calor. Recomendación: limpieza profunda."
        ))

    @Rule(Sintoma(flujo_aire='No estoy seguro'))
    def recomendacion_revision_aire(self):
        self.declare(Sintoma(
            diagnostico="Posible mala disipación térmica. Verificar suciedad, protectores plásticos o accesorios que bloqueen el paso de aire."
        ))

    @Rule(Sintoma(flujo_aire='Sí'))
    def preguntar_nivel_aceite(self):
        self.declare(Sintoma(
            key="nivel_aceite",
            pregunta="¿El nivel de aceite del motor es el adecuado?",
            opciones=["Bajo", "Normal", "No sé"]
        ))

    @Rule(Sintoma(nivel_aceite='Bajo'))
    def bajo_aceite(self):
        self.declare(Sintoma(
            diagnostico="Nivel de aceite bajo. Aumenta fricción, temperatura y desgaste interno. Recomendación: rellenar o cambiar aceite inmediatamente."
        ))

    @Rule(Sintoma(nivel_aceite='No sé'))
    def sugerir_revision_aceite(self):
        self.declare(Sintoma(
            diagnostico="Es necesario verificar el nivel de aceite. Sobrecalentamiento podría estar relacionado con lubricación insuficiente."
        ))

    @Rule(Sintoma(nivel_aceite='Normal'))
    def preguntar_bujia(self):
        self.declare(Sintoma(
            key="estado_bujia",
            pregunta="¿La bujía sale blanca o muy limpia al retirarla?",
            opciones=["Sí", "No", "No la he revisado"]
        ))

    @Rule(Sintoma(estado_bujia='Sí'))
    def mezcla_pobre(self):
        self.declare(Sintoma(
            diagnostico="Bujía blanca indica mezcla pobre o entrada excesiva de aire. Revisar carburador, filtro de aire y posibles fugas de admisión."
        ))

    @Rule(Sintoma(estado_bujia='No'))
    def posible_conduccion(self):
        self.declare(Sintoma(
            diagnostico="El sobrecalentamiento podría deberse a conducción prolongada a altas RPM, baja velocidad con motor forzado o desgaste interno del motor. Se recomienda revisión mecánica."
        ))

    @Rule(Sintoma(estado_bujia='No la he revisado'))
    def recomendar_revision_bujia(self):
        self.declare(Sintoma(
            diagnostico="La bujía es clave para diagnosticar temperatura y mezcla. Se recomienda inspección para diagnóstico preciso."
        ))

    # ───────────────────────────────────────────────
    # RAMA — NINGÚN SÍNTOMA
    # ───────────────────────────────────────────────

    @Rule(Sintoma(sintoma_motor='Ninguno'))
    def motor_ok(self):
        self.declare(Sintoma(
            diagnostico=(
                "No se detectan fallas en el motor.\n"
                "Recomendación: mantenimiento preventivo cada 3.000 a 5.000 km."
            )
        ))


    # ───────────────────────────────────────────────
    # SISTEMA EXPERTO — SUSPENSIÓN
    # ───────────────────────────────────────────────

    @Rule(Sintoma(diagnostico_inicial='Suspensión'))
    def inicio_suspension(self):
        self.declare(Sintoma(
            key="sintoma_suspension",
            pregunta="¿Qué síntoma presenta la suspensión?",
            opciones=[
                "Rebote excesivo",
                "Hundimiento al frenar",
                "Golpeteos o ruidos",
                "Suspensión muy dura",
                "Dirección inestable",
                "Desgaste irregular de llantas",
                "Fuga de aceite en barras",
                "Ninguno"
            ]
        ))


    # ───────────────────────────────────────────────
    # RAMA — REBOTE EXCESIVO
    # ───────────────────────────────────────────────

    @Rule(Sintoma(sintoma_suspension='Rebote excesivo'))
    def preguntar_amortiguador(self):
        self.declare(Sintoma(
            key="estado_amortiguador",
            pregunta="¿El rebote ocurre adelante, atrás o en ambos?",
            opciones=["Delantero", "Trasero", "Ambos"]
        ))


    @Rule(Sintoma(estado_amortiguador='Delantero'))
    def diagnostico_delantero_rebote(self):
        self.declare(Sintoma(
            diagnostico="Amortiguadores delanteros sin capacidad de amortiguación. Probable aceite degradado o resortes fatigados."
        ))


    @Rule(Sintoma(estado_amortiguador='Trasero'))
    def diagnostico_trasero_rebote(self):
        self.declare(Sintoma(
            diagnostico="Amortiguador trasero con fuga interna o desgaste del cartucho. Reemplazo recomendado."
        ))


    @Rule(Sintoma(estado_amortiguador='Ambos'))
    def diagnostico_ambos_rebote(self):
        self.declare(Sintoma(
            diagnostico="Sistema de suspensión debilitado. Requiere revisión completa de amortiguadores, aceite y resortes."
        ))


    # ───────────────────────────────────────────────
    # RAMA — HUNDIMIENTO AL FRENAR (NOSE DIVE)
    # ───────────────────────────────────────────────

    @Rule(Sintoma(sintoma_suspension='Hundimiento al frenar'))
    def preguntar_aceite_barras(self):
        self.declare(Sintoma(
            key="nivel_aceite_barras",
            pregunta="¿Se ha cambiado el aceite de horquillas recientemente?",
            opciones=["Sí", "No"]
        ))


    @Rule(Sintoma(nivel_aceite_barras='No'))
    def diagnostico_falta_mantenimiento(self):
        self.declare(Sintoma(
            diagnostico="Aceite de suspensión degradado reduce amortiguación. Reemplazar y calibrar viscosidad."
        ))


    @Rule(Sintoma(nivel_aceite_barras='Sí'))
    def preguntar_resortes(self):
        self.declare(Sintoma(
            key="estado_resortes",
            pregunta="¿La moto tiene muchos kilómetros o carga frecuente?",
            opciones=["Sí", "No"]
        ))


    @Rule(Sintoma(estado_resortes='Sí'))
    def diagnostico_resortes(self):
        self.declare(Sintoma(
            diagnostico="Resortes fatigados. Reemplazo o aumento de precarga recomendado."
        ))


    @Rule(Sintoma(estado_resortes='No'))
    def diagnostico_frenos_geometria(self):
        self.declare(Sintoma(
            diagnostico="Posible desbalance entre frenos y suspensión. Revisar retenes, alineación y SAG."
        ))


    # ───────────────────────────────────────────────
    # RAMA — GOLPETEOS O RUIDOS
    # ───────────────────────────────────────────────

    @Rule(Sintoma(sintoma_suspension='Golpeteos o ruidos'))
    def preguntar_origen_ruido(self):
        self.declare(Sintoma(
            key="origen_ruido_susp",
            pregunta="¿El ruido ocurre al pasar baches o en terreno plano?",
            opciones=["Solo en baches", "Siempre"]
        ))


    @Rule(Sintoma(origen_ruido_susp='Solo en baches'))
    def diagnostico_bujes(self):
        self.declare(Sintoma(
            diagnostico="Posible juego en bujes, rodamientos del basculante o pernos sueltos."
        ))


    @Rule(Sintoma(origen_ruido_susp='Siempre'))
    def diagnostico_tuercas_direccion(self):
        self.declare(Sintoma(
            diagnostico="Juego en dirección o rodamientos de la tija. Ajuste o reemplazo necesario."
        ))


    # ───────────────────────────────────────────────
    # RAMA — SUSPENSIÓN MUY DURA
    # ───────────────────────────────────────────────

    @Rule(Sintoma(sintoma_suspension='Suspensión muy dura'))
    def preguntar_precarga(self):
        self.declare(Sintoma(
            key="precarga",
            pregunta="¿La precarga del amortiguador está aumentada?",
            opciones=["Sí", "No", "No se sabe"]
        ))


    @Rule(Sintoma(precarga='Sí'))
    def diagnostico_precarga_alta(self):
        self.declare(Sintoma(
            diagnostico="Precarga excesiva endurece suspensión. Reducir al nivel recomendado por fabricante."
        ))


    @Rule(Sintoma(precarga='No'))
    def diagnostico_resorte_rigido(self):
        self.declare(Sintoma(
            diagnostico="Resortes demasiado rígidos para el peso del conductor. Considerar cambio."
        ))


    @Rule(Sintoma(precarga='No se sabe'))
    def diagnostico_ajuste(self):
        self.declare(Sintoma(
            diagnostico="Suspensión sin calibración adecuada. Ajustar SAG, precarga y rebote."
        ))


    # ───────────────────────────────────────────────
    # RAMA — DIRECCIÓN INESTABLE / SERPENTEO
    # ───────────────────────────────────────────────

    @Rule(Sintoma(sintoma_suspension='Dirección inestable'))
    def preguntar_llantas(self):
        self.declare(Sintoma(
            key="presion_llantas",
            pregunta="¿La presión de las llantas es adecuada?",
            opciones=["Sí", "No"]
        ))


    @Rule(Sintoma(presion_llantas='No'))
    def diagnostico_inflado(self):
        self.declare(Sintoma(
            diagnostico="Presión incorrecta altera estabilidad. Ajustar a rango recomendado."
        ))


    @Rule(Sintoma(presion_llantas='Sí'))
    def preguntar_rodamientos(self):
        self.declare(Sintoma(
            key="rodamientos_direccion",
            pregunta="¿Se percibe ruido o juego en la dirección al frenar?",
            opciones=["Sí", "No"]
        ))


    @Rule(Sintoma(rodamientos_direccion='Sí'))
    def diagnostico_juego_direccion(self):
        self.declare(Sintoma(
            diagnostico="Rodamientos de dirección desgastados o flojos."
        ))


    @Rule(Sintoma(rodamientos_direccion='No'))
    def diagnostico_amortiguador_direccion(self):
        self.declare(Sintoma(
            diagnostico="Posible amortiguador de dirección dañado o mala alineación."
        ))


    # ───────────────────────────────────────────────
    # RAMA — DESGASTE IRREGULAR DE LLANTAS
    # ───────────────────────────────────────────────

    @Rule(Sintoma(sintoma_suspension='Desgaste irregular de llantas'))
    def preguntar_alineacion(self):
        self.declare(Sintoma(
            key="alineacion",
            pregunta="¿La llanta trasera está visualmente alineada?",
            opciones=["Sí", "No"]
        ))


    @Rule(Sintoma(alineacion='No'))
    def diagnostico_mala_alineacion(self):
        self.declare(Sintoma(
            diagnostico="Basculante o eje mal alineado. Ajustar para evitar desgaste prematuro."
        ))


    @Rule(Sintoma(alineacion='Sí'))
    def diagnostico_susp_tension(self):
        self.declare(Sintoma(
            diagnostico="Suspensión desbalanceada o amortiguador debilitado afecta desgaste."
        ))


    # ───────────────────────────────────────────────
    # RAMA — FUGA DE ACEITE EN BARRAS
    # ───────────────────────────────────────────────

    @Rule(Sintoma(sintoma_suspension='Fuga de aceite en barras'))
    def diagnostico_retenes(self):
        self.declare(Sintoma(
            diagnostico="Retenes deteriorados o barra rayada. Reemplazo urgente para evitar pérdida de amortiguación."
        ))


    # ───────────────────────────────────────────────
    # SIN SÍNTOMAS
    # ───────────────────────────────────────────────

    @Rule(Sintoma(sintoma_suspension='Ninguno'))
    def suspension_ok(self):
        self.declare(Sintoma(
            diagnostico="Suspensión en condiciones normales. Mantener lubricación, limpieza y revisión periódica."
        ))
