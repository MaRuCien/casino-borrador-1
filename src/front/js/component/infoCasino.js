import React, { useContext } from "react";
import { Context } from "../store/appContext";
import '../../styles/adminEmpresa.css'

function  InformacionCasino() {
  const { store } = useContext(Context);
  return (
    <>
    <table  className="table mt-5" >
      <div  className="card">
        {!!store.infocasino &&
          store.infocasino.map((casino, i) => {
            <ul key={i} className="list-group list-group-flush">
              <li className="casino">Nombre: {casino.nombre}</li>
              <li className="casino">Teléfono: {casino.telefono}</li>
              <li className="casino">Dirección: {casino.direccion}</li>
              <li className="casino">Correo electrónico: {casino.email}</li>
            </ul>
          })
        }
      </div>
    </table>;
    </>
  );
}

export default InformacionCasino;
