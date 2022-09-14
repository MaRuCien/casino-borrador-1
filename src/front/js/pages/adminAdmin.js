import React from 'react'
import { Link } from 'react-router-dom'
import '../../styles/adminEmpresa.css'
import InfoCasino from '../component/infoCasino';
import Usuarios from '../component/infoUsuarios';

const DetalleEmpresa = () => {
    return (

        <div className="container mt-5">
        <div className="row">
            <div className="col-12 mt-5">
                <div className="my-5">
                    <h3>Información para empresa</h3>
                    <hr />
                    El casino que se ocupa de tu empresa es:
                    <InfoCasino />
                    <hr/>
                    Los usuarios que corresponden a tu empresa:
                    <table className="table mt-3">
                        <thead>
                            <tr>
                                <th scope="col">Id</th>
                                <th scope="col">Nombre</th>
                                <th scope="col">Apellido</th>
                                <th scope="col">Dirección</th>
                                <th scope="col">Teléfono</th>
                            </tr>
                        </thead>
                    <Usuarios />
                    </table>
                    <div className=''>
                        <Link to="/admin-casino"><button className='btn btn-success'>Crear Menú</button></Link>
                        <Link to="/menu-casino"><button className='btn btn-success'>Ver Menú</button></Link>
                    </div>
                </div>

            </div>
        </div>
    </div>



    );
}


export default DetalleEmpresa;