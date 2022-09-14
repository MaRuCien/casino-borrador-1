import React, { useContext } from "react";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom";

function Usuarios() {
  const { store } = useContext(Context);
  return (
    <>
      {!!store.get_usuarios &&
        store.get_usuarios.map((usuario, i) => {
          return (
            <tbody  key={i}>
              <tr>
                <th scope="row">
                  {usuario.id}
                </th>
                <td>{usuario.nombre}</td>
                <td>{usuario.apellido}</td>
                <td>{usuario.direccion}</td>
                <td>{usuario.telefono}</td>
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

export default Usuarios;
