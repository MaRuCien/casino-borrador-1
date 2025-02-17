"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, Usuario, Empresa, Casino, Menu, Dia, Reporte_Usuario, Decision_Almuerzo
from api.utils import generate_sitemap, APIException
import os
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

api = Blueprint('api', __name__)


# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@api.route("/token", methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)


##Registro usuario, empresa y casino

@api.route('/register', methods=['POST'])
def Usuario_add():
    request_body_usuario = request.get_json()

    nombre = request.json.get('nombre', None)
    apellido = request.json.get('apellido', None)
    telefono = request.json.get('telefono', None)
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    direccion = request.json.get('direccion', None)
    empresa_id = request.json.get('empresa_id', None)

    if nombre is None:
        return 'Escriba su nombre', 400
    if apellido is None:
        return 'Escriba su apellido', 400
    if telefono is None:
        return 'Escriba su telefono', 400
    if email is None:
        return 'Escriba su email', 400
    if password is None:
        return 'Escriba su password', 400
    if direccion is None:
        return 'Escriba su direccion', 400
    if empresa_id is None:
        return 'Escriba su empresa', 400

    usuario = Usuario.query.filter_by(email=email).first()

    if usuario:
        return jsonify({"msg": "User already exists"})
    else:
        new_usuario = Usuario(nombre=request_body_usuario['nombre'],
                              apellido=request_body_usuario['apellido'],
                              telefono=request_body_usuario['telefono'],
                              email=request_body_usuario['email'],
                              password=request_body_usuario['password'],
                              direccion=request_body_usuario['direccion'],
                              empresa_id=request_body_usuario['empresa_id']
                              )
        db.session.add(new_usuario)
        db.session.commit()
        return jsonify({"msg": "Usuario creado!"}), 200


@api.route('/registro', methods=['POST'])
def Empresa_add():
    request_body_empresa = request.get_json()

    nombre = request.json.get('nombre', None)
    telefono = request.json.get('telefono', None)
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    direccion = request.json.get('direccion', None)

    if nombre is None:
        return 'Escriba el nombre de empresa', 400
    if telefono is None:
        return 'Escriba el telefono de la empresa', 400
    if email is None:
        return 'Escriba el email de empresa', 400
    if password is None:
        return 'Escriba su password', 400
    if direccion is None:
        return 'Escriba la direccion de la empresa', 400

    empresa = Empresa.query.filter_by(email=email).first()

    if empresa:
        return jsonify({"msg": "Esta empresa se encuentra registrada"})
    else:
        new_empresa = Empresa(nombre=request_body_empresa['nombre'],
                              telefono=request_body_empresa['telefono'],
                              email=request_body_empresa['email'],
                              password=request_body_empresa['password'],
                              direccion=request_body_empresa['direccion'],
                              )
        db.session.add(new_empresa)
        db.session.commit()
        return jsonify({"msg": "¡Se registró la empresa con éxito!"}), 200



@api.route('/registro-casino', methods=['POST'])
def Casino_add():
    request_body_casino = request.get_json()

    nombre = request.json.get('nombre', None)
    telefono = request.json.get('telefono', None)
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    direccion = request.json.get('direccion', None)

    if nombre is None:
        return 'Escriba el nombre del casino', 400
    if telefono is None:
        return 'Escriba el telefono del casino', 400
    if email is None:
        return 'Escriba el email del casino', 400
    if password is None:
        return 'Escriba el password del casino', 400
    if direccion is None:
        return 'Escriba la direccion del casino', 400

    casino = Casino.query.filter_by(email=email).first()

    if casino:
        return jsonify({"msg": "Este casino ya se encuentra registrado"})
    else:
        new_casino = Casino(nombre=request_body_casino['nombre'],
                              telefono=request_body_casino['telefono'],
                              email=request_body_casino['email'],
                              password=request_body_casino['password'],
                              direccion=request_body_casino['direccion'],
                              )
        db.session.add(new_casino)
        db.session.commit()
        return jsonify({"msg": "¡Se registró el casino con éxito!"}), 200


## Login usuario, empresa y casino
@api.route('/login/user', methods=['POST'])
def login_usuario():
    body = request.get_json()

    email = request.json.get('email',None)
    password = request.json.get('password', None)

    usuario = Usuario.query.filter_by(email=email, password = password).first()
    if not usuario:
        return jsonify({"msg":"Usuario/Contraseña no coinciden"}), 400

    access_token  = create_access_token(identity=usuario.email)

    data ={
        "user": usuario.serialize(),
        "access_token":access_token
    }

    return jsonify(data), 200


@api.route('/login/empresa', methods=['POST'])
def login_empresa():
    body = request.get_json()

    email = request.json.get('email',None)
    password = request.json.get('password', None)

    empresa = Empresa.query.filter_by(email=email, password = password).first()
    if not empresa:
        return jsonify({"msg":"Empresa/Contraseña no coinciden"}), 400

    access_token  = create_access_token(identity=empresa.email)

    data ={
        "empresa": empresa.serialize(),
        "access_token":access_token
    }

    return jsonify(data), 200


@api.route('/login/casino', methods=['POST'])
def login_casino():
    body = request.get_json()

    email = request.json.get('email',None)
    password = request.json.get('password', None)

    casino = Casino.query.filter_by(email=email, password = password).first()
    if not casino:
        return jsonify({"msg":"Casino/Contraseña no coinciden"}), 400

    access_token  = create_access_token(identity=casino.email)

    data ={
        "casino": casino.serialize(),
        "access_token":access_token
    }

    return jsonify(data), 200

#Para las páginas privadas

@api.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200



#creación, actualización y eliminación de empresa | también get para verlas
@api.route('empresa', methods=['GET', 'POST'])
@api.route('empresa/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_company(id = None):
    if request.method == 'GET':
        if id is not None:
            empresa: Empresa.query.get(id)
            if not empresa: return jsonify({ "msg": "No encontramos la empresa" }), 404
            return jsonify(empresa.serialize()), 200
        else:
            empresas = Empresa.query.all()
            empresas = list(map(lambda empresa: empresa.serialize(), empresas))

            return jsonify(empresas), 200
    
    if request.method == 'POST':
        nombre = request.json.get("nombre")
        telefono = request.json.get("telefono")
        email = request.json.get("email")
        direccion = request.json.get("direccion", "")
        password = request.json.get("password")
 

        if not nombre: return jsonify({ "msg": "El nombre es obligatorio" }), 400
        if not telefono: return jsonify({ "msg": "El teléfono es obligatorio" }), 400
        if not email: return jsonify({ "msg": "La email es obligatoria" }), 400
        if not password: return jsonify({ "msg": "El password es obligatorio" }), 400

        empresa = Empresa()
        empresa.nombre = nombre
        empresa.telefono = telefono
        empresa.email = email
        empresa.direccion = direccion
        empresa.password = password
        empresa.save()

        return jsonify(empresa.serialize()), 201
    
    if request.method == 'PUT':
        nombre = request.json.get("nombre")
        telefono = request.json.get("telefono")
        email = request.json.get("email")
        direccion = request.json.get("direccion", "")
        password = request.json.get("password")
 

        if not nombre: return jsonify({ "msg": "El nombre es obligatorio" }), 400
        if not telefono: return jsonify({ "msg": "El teléfono es obligatorio" }), 400
        if not email: return jsonify({ "msg": "El email es obligatorio" }), 400
        if not password: return jsonify({ "msg": "El password es obligatorio" }), 400

        empresa = Empresa.query.get(id)
        if not empresa: return jsonify({ "msg": "No encontramos la empresa" }), 404
        empresa.nombre = nombre
        empresa.telefono = telefono
        empresa.email = email
        empresa.direccion = direccion
        empresa.password = password
        empresa.update()

        return jsonify(empresa.serialize()), 200
    
    if request.method == 'DELETE':
        empresa = Empresa.query.get(id)
        if not empresa: return jsonify({ "msg": "No encontramos la empresa" }), 404

        empresa.delete()
        return jsonify({ "msg": "Empresa eliminada" }), 200


#La empresa crea contactos, puede obtenerlos todo, a uno de ellos, actualizar o borrar:
@api.route('empresa/usuarios', methods=['GET', 'POST'])
@api.route('empresa/usuarios/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_users(id = None):
    if request.method == 'GET':
        if id is not None:
            usuario: Usuario.query.get(id)
            if not usuario: return jsonify({ "msg": "No encontramos el usuario" }), 404
            return jsonify(usuario.serialize()), 200
        else:
            usuarios = Usuario.query.all()
            usuarios = list(map(lambda usuario: usuario.serialize(), usuarios))

            return jsonify(usuarios), 200
    
    if request.method == 'POST':
        nombre = request.json.get("nombre")
        apellido = request.json.get("apellido")
        telefono = request.json.get("telefono")
        email = request.json.get("email")
        direccion = request.json.get("direccion", "")
        password = request.json.get("password") 
        empresa_id = request.json.get("empresa_id")   
    
        if not nombre: return jsonify({ "msg": "El nombre es obligatorio" }), 400
        if not apellido: return jsonify({ "msg": "El apellido es obligatorio" }), 400
        if not telefono: return jsonify({ "msg": "El teléfono es obligatorio" }), 400
        if not email: return jsonify({ "msg": "El email es obligatorio" }), 400
        if not password: return jsonify({ "msg": "El password es obligatorio" }), 400
        if not empresa_id: return jsonify({ "msg": "La empresa es obligatorio" }), 400

        usuario = Usuario()
        usuario.nombre = nombre
        usuario.apellido = apellido
        usuario.telefono = telefono
        usuario.email = email
        usuario.direccion = direccion
        usuario.password = password
        usuario.empresa_id = empresa_id
        usuario.save()

        return jsonify(usuario.serialize()), 201

    if request.method == 'PUT':
        nombre = request.json.get("nombre")
        telefono = request.json.get("telefono")
        email = request.json.get("email")
        direccion = request.json.get("direccion", "")
        password = request.json.get("password")
 

        if not nombre: return jsonify({ "msg": "El nombre es obligatorio" }), 400
        if not telefono: return jsonify({ "msg": "El teléfono es obligatorio" }), 400
        if not email: return jsonify({ "msg": "El email es obligatorio" }), 400
        if not password: return jsonify({ "msg": "El password es obligatorio" }), 400

        usuario = Usuario.query.get(id)
        if not usuario: return jsonify({ "msg": "No encontramos el usuario" }), 404
        usuario.nombre = nombre
        usuario.telefono = telefono
        usuario.email = email
        usuario.direccion = direccion
        usuario.password = password
        usuario.update()

        return jsonify(usuario.serialize()), 200
    
    if request.method == 'DELETE':
        usuario = Usuario.query.get(id)
        if not usuario: return jsonify({ "msg": "No encontramos el usuario" }), 404

        usuario.delete()
        return jsonify({ "msg": "Usuario eliminado" }), 200

#Get a la empresa con sus usuarios
@api.route('empresa/lista-usuarios', methods=['GET'])
def get_users_company():
    if request.method == 'GET':

            empresas = Empresa.query.all()
            empresas = list(map(lambda empresa: empresa.serialize_con_usuarios(), empresas))

            return jsonify(empresas), 200

#El usuario necesita un post para el login | un put para actualizar 
@api.route('/login/user', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    usuario = Usuario.query.filter_by(email=email).first()
    if not usuario:
        return jsonify({"msg":"Usuario/Contraseña no coinciden"}), 400

    if not check_password_hash(usuario.password, password): 
        return jsonify({"msg":"Usuario/Contraseña no coinciden"}), 400

    access_token  = create_access_token(identity=usuario.email)

    data ={
        "access_token":access_token,
        "user": usuario.serialize()

    }

    return jsonify(data), 200

#El usuario necesita un put para actualizar sus datos
@api.route('usuario', methods=['GET', 'POST'])
@api.route('usuario/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def acutalizacion_datos(id = None):

    if request.method == 'GET':
        if id is not None:
            usuario: Usuario.query.get(id)
            if not usuario: return jsonify({ "msg": "No encontramos la empresa" }), 404
            return jsonify(usuario.serialize()), 200
        else:
            usuarios = Usuario.query.all()
            usuarios = list(map(lambda usuario: usuario.serialize(), usuarios))

            return jsonify(usuarios), 200
    
    if request.method == 'POST':
        nombre = request.json.get("nombre")
        telefono = request.json.get("telefono")
        email = request.json.get("email")
        direccion = request.json.get("direccion", "")
        password = request.json.get("password")
 

        if not nombre: return jsonify({ "msg": "El nombre es obligatorio" }), 400
        if not telefono: return jsonify({ "msg": "El teléfono es obligatorio" }), 400
        if not email: return jsonify({ "msg": "La email es obligatoria" }), 400
        if not password: return jsonify({ "msg": "El password es obligatorio" }), 400

        usuario = Usuario()
        usuario.nombre = nombre
        usuario.telefono = telefono
        usuario.email = email
        usuario.direccion = direccion
        usuario.password = password
        usuario.save()

        return jsonify(usuario.serialize()), 201
    
    if request.method == 'PUT':
        nombre = request.json.get("nombre")
        telefono = request.json.get("telefono")
        email = request.json.get("email")
        direccion = request.json.get("direccion", "")
        password = request.json.get("password")
 

        if not nombre: return jsonify({ "msg": "El nombre es obligatorio" }), 400
        if not telefono: return jsonify({ "msg": "El teléfono es obligatorio" }), 400
        if not email: return jsonify({ "msg": "El email es obligatorio" }), 400
        if not password: return jsonify({ "msg": "El password es obligatorio" }), 400

        usuario = Usuario.query.get(id)
        if not usuario: return jsonify({ "msg": "No encontramos al usuario" }), 404
        usuario.nombre = nombre
        usuario.telefono = telefono
        usuario.email = email
        usuario.direccion = direccion
        usuario.password = password
        usuario.update()

        return jsonify(usuario.serialize()), 200
    
    if request.method == 'DELETE':
        usuario = Usuario.query.get(id)
        if not usuario: return jsonify({ "msg": "No encontramos al usuario" }), 404

        usuario.delete()
        return jsonify({ "msg": "Usuario eliminado" }), 200

#Creación, actualización y delete de casino
@api.route('casino', methods=['GET', 'POST'])
@api.route('casino/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_casino(id = None):


    if request.method == 'GET':
        if id is not None:
            casino: Casino.query.get(id)
            if not casino: return jsonify({ "msg": "No encontramos el casino" }), 404
            return jsonify(casino.serialize()), 200
        else:
            casinos = Casino.query.all()
            casinos = list(map(lambda casino: casino.serialize(), casinos))

            return jsonify(casinos), 200
    
    if request.method == 'POST':
        nombre = request.json.get("nombre")
        telefono = request.json.get("telefono")
        email = request.json.get("email")
        direccion = request.json.get("direccion", "")
        password = request.json.get("password")
 

        if not nombre: return jsonify({ "msg": "El nombre es obligatorio" }), 400
        if not telefono: return jsonify({ "msg": "El teléfono es obligatorio" }), 400
        if not email: return jsonify({ "msg": "La email es obligatoria" }), 400
        if not password: return jsonify({ "msg": "El password es obligatorio" }), 400

        casino = Casino()
        casino.nombre = nombre
        casino.telefono = telefono
        casino.email = email
        casino.direccion = direccion
        casino.password = password
        casino.save()

        return jsonify(casino.serialize()), 201
    
    if request.method == 'PUT':
        nombre = request.json.get("nombre")
        telefono = request.json.get("telefono")
        email = request.json.get("email")
        direccion = request.json.get("direccion", "")
        password = request.json.get("password")
 

        if not nombre: return jsonify({ "msg": "El nombre es obligatorio" }), 400
        if not telefono: return jsonify({ "msg": "El teléfono es obligatorio" }), 400
        if not email: return jsonify({ "msg": "El email es obligatorio" }), 400
        if not password: return jsonify({ "msg": "El password es obligatorio" }), 400

        casino = Casino.query.get(id)
        if not casino: return jsonify({ "msg": "No encontramos el casino" }), 404
        casino.nombre = nombre
        casino.telefono = telefono
        casino.email = email
        casino.direccion = direccion
        casino.password = password
        casino.update()

        return jsonify(casino.serialize()), 200

    if request.method == 'DELETE':
        casino = Casino.query.get(id)
        if not casino: return jsonify({ "msg": "No encontramos el casino" }), 404

        casino.delete()
        return jsonify({ "msg": "Casino eliminado" }), 200

# Ver la empresa y los usuarios asignados a un casino #quedó error pendiente por ver
@api.route('casino/empresa', methods=['GET'])
def lista_empresa():
    listas: Casino.query.all()
    listas: list(map(lambda lista: lista.serialize_casino_empresa(), listas))

    return jsonify(listas), 200

@api.route('problema-usuario', methods=['GET', 'POST'])
@api.route('problema-usuario/<int:id>', methods=['GET'])
def Problema_usuario(id = None):
    if request.method == 'GET':
        if id is not None:
            request.method: Reporte_Usuario.query.get(id)
            if not reporte_usuario: return jsonify({ "msg": "No encontramos este reporte" }), 404
            return jsonify(reporte_usuario.serialize()), 200
        else:
            reportes_usuario = Reporte_Usuario.query.all()
            reportes_usuario = list(map(lambda reporte_usuario: reporte_usuario.serialize(), reportes_usuario))

            return jsonify(reportes_usuario), 200
    
    if request.method == 'POST':
        contenido = request.json.get("contenido")
        usuario_id = request.json.get("usuario_id")  
    
        if not contenido: return jsonify({ "msg": "Favor reportar problema" }), 400
        
        reporte_usuario = Reporte_Usuario()
        reporte_usuario.contenido = contenido
        reporte_usuario.usuario_id = usuario_id


        reporte_usuario.save()

        return jsonify(reporte_usuario.serialize()), 201
#decision de almuerzo
@api.route('decision-almuerzo', methods=['GET', 'POST'])
@api.route('decision-almuerzo/<int:id>', methods=['GET'])
def D_almuerzo(id = None):
    if request.method == 'GET':
        if id is not None:
            request.method: Decision_Almuerzo.query.get(id)
            if not decision_almuerzo: return jsonify({ "msg": "No registramos su decision de Almuerzo" }), 404
            return jsonify(decision_almuerzo.serialize()), 200
        else:
            decision_almuerzo = Decision_Almuerzo.query.all()
            decision_almuerzo = list(map(lambda decision_almuerzo: decision_almuerzo.serialize(), decision_almuerzo))

            return jsonify(decision_almuerzo), 200

    if request.method == 'POST':
        decision = request.json.get("decision")
        usuario_id = request.json.get("usuario_id")  

        if not decision: return jsonify({ "msg": "Favor reportar problema" }), 400

        decision_almuerzo = Decision_Almuerzo()
        decision_almuerzo.decision = decision
        decision_almuerzo.usuario_id = usuario_id


        decision_almuerzo.save()

        return jsonify(decision_almuerzo.serialize()), 201

# menús
@api.route('/menu', methods=['GET'])
def all_menus():
    if request.method == 'GET':
        menus = Menu.query.all()
        menus = list(map(lambda menu: menu.serialize(), menus))

        return jsonify(menus), 200
#Crear un menú nuevo
@api.route('/menu', methods=['POST'])
def create_menu():
    if request.method == 'POST':
        principal = request.json.get("principal")
        ensalada = request.json.get("ensalada")
        postre = request.json.get("postre")
        bebida = request.json.get("bebida")
 

        if not principal: return jsonify({ "msg": "Tiene que ofrecer un plato principal" }), 400
        if not ensalada: return jsonify({ "msg": "Tiene que ofrecer una ensalada" }), 400
        if not postre: return jsonify({ "msg": "Tiene que ofrecer un postre" }), 400
        if not bebida: return jsonify({ "msg": "Tiene que ofrecer una bebida" }), 400

        menu = Menu()
        menu.principal = principal
        menu.ensalada = ensalada
        menu.postre = postre
        menu.bebida = bebida
        menu.save()

        return jsonify(menu.serialize()), 201
#Obtener un menú específico
@api.route('/menu/<int:id>', methods=['GET'])
def get_menu(id):
    if not Menu.query.get(id): return jsonify({ "msg": "No encontramos el menu" }), 404
    return jsonify(Menu.query.get(id).serialize()), 200
#Actualizar el menú
@api.route('/menu/<int:id>', methods=['PUT'])
def update_menu(id):
        principal = request.json.get("principal")
        ensalada = request.json.get("ensalada")
        postre = request.json.get("postre")
        bebida = request.json.get("bebida")
 

        if not principal: return jsonify({ "msg": "Tiene que ofrecer un plato principal" }), 400
        if not ensalada: return jsonify({ "msg": "Tiene que ofrecer una ensalada" }), 400
        if not postre: return jsonify({ "msg": "Tiene que ofrecer un postre" }), 400
        if not bebida: return jsonify({ "msg": "Tiene que ofrecer una bebida" }), 400

        menu = Menu()
        menu.principal = principal
        menu.ensalada = ensalada
        menu.postre = postre
        menu.bebida = bebida
        menu.update()

        return jsonify(menu.serialize()), 200
#Borrar un menú específico    
@api.route('/menu/<int:id>', methods=['DELETE'])
def delete_menu(id):    
    if request.method == 'DELETE':
        menu = Menu.query.get(id)
        if not menu: return jsonify({ "msg": "No encontramos el menú" }), 404

        menu.delete()
        return jsonify({ "msg": "Menú eliminado" }), 200
#Conseguir los días creados
@api.route('/dia', methods=['GET'])
def all_dias():
    if request.method == 'GET':
        dias = Dia.query.all()
        dias = list(map(lambda dia: dia.serialize(), dias))

        return jsonify(dias), 200
#Crear un día
@api.route('/dia', methods=['POST'])
def crear_dia():
        dia = request.json.get("dia")

        if not dia: return jsonify({ "msg": "El día debe ser asignado" }), 400
        
        new_dia = Dia()
        new_dia.dia = dia
        new_dia.save()

        return jsonify(new_dia.serialize()), 201
    
#Mostrar un menú con el día asignado
@api.route('/dia/menus', methods=['GET'])
def get_menu_with_dia():
        dias  = Dia.query.all()
        dias = list(map(lambda dia: dia.serialize_with_menus(), dias))

        return jsonify(dias), 200


#Crear un menú con día asignado
@api.route('/dia/menus', methods=['POST'])
def create_menu_with_dia():

    #traigo los datos
    dia = request.json.get('dia')

    principal = request.json.get('principal')
    ensalada = request.json.get('ensalada')
    postre = request.json.get('postre')
    bebida = request.json.get('bebida')

    new_dia = Dia()
    new_dia.dia = dia

    menu = Menu()
    menu.principal = principal
    menu.ensalada = ensalada
    menu.postre = postre
    menu.bebida = bebida

    new_dia.menu = menu
    new_dia.save()

    return jsonify(new_dia.serialize_with_menus()), 201

#Actualizar un menú con día asignado
@api.route('/dia/menus/<int:id>', methods=['PUT'])
def update_menu_with_dia(id):

    #traigo los datos
    dia = request.json.get('dia')

    principal = request.json.get('principal')
    ensalada = request.json.get('ensalada')
    postre = request.json.get('postre')
    bebida = request.json.get('bebida')

    new_dia = Dia()
    new_dia.dia = dia

    menu = Menu()
    menu.principal = principal
    menu.ensalada = ensalada
    menu.postre = postre
    menu.bebida = bebida

    new_dia.menu = menu
    new_dia.save()

    return jsonify(new_dia.serialize_with_menus()), 200

#Día y Menú asignado, de forma individual
@api.route('/dia/menus/<int:id>', methods=['GET'])
def get_menu_with_diaById(id):
    if not Dia.query.get(id): return jsonify({ "msg": "No encontramos el menu" }), 404
    return jsonify(Dia.query.get(id).serialize_with_menus()), 200

#Mostrar decision con su usuario
@api.route('/entregas', methods=['GET'])
def get_entregas():
        decisiones  = Decision.query.all()
        decisiones = list(map(lambda decision: decision.serialize(), decisiones))

        return jsonify(decisiones), 200


#Crear la vista de entregas
@api.route('/entregas', methods=['POST'])
def create_entrega():

    #traigo los datos
    entrega = request.json.get('decision')

    nombre = request.json.get('nombre')
    apellido = request.json.get('apellido')
    telefono = request.json.get('telefono')
    direccion = request.json.get('direccion')

    entrega = Decision()
    entrega.decision = decision

    usuario = Usuario()
    usuario.nombre = nombre
    usuario.apellido = apellido
    usuario.telefono = telefono
    usuario.direccion = direccion

    entrega.usuario = entrega
    entrega.save()

    return jsonify(entrega.serialize()), 201