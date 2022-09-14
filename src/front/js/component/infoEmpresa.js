import React, { useContext } from "react";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom";


function InfoEmpresa() {
  const { store } = useContext(Context);
  return (
    <>
      {!!store.get_empresa &&
        store.get_empresa.map((empresa, i) => {
          return (
            <tbody>
              <tr>
                <th scope="row" key={i}>
                  {empresa.id}
                </th>
                <td>{empresa.nombre}</td>
                <td>{empresa.direccion}</td>
                <td>{empresa.email}</td>
                <td>{empresa.telefono}</td>
                <Link to="/">
                  <button type="button" className="btn btn-success btn-lg mt-1">
                    Mapa
                  </button>
                </Link>
              </tr>
            </tbody>
          );
        })}
    </>
  );
}

export default InfoEmpresa;