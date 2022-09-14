import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";

const DireccionesUsuario = () => {
  const { store } = useContext(Context);

  return (
    <div className="container mt-5">
      <div className="row">
        <div className="col-12 mt-5">
          <div className="my-5">
            <h3>Direcciones de Usuario</h3>
            <hr />
          </div>

          <form className="file-upload">
            <div className="row mb-5 gx-5">
              <div className="col-xxl-8 mb-5 mb-xxl-0">
                <div className="bg-secondary-soft px-4 py-5 rounded">
                  <div className="row g-3">
                    <div className="col-md-7">
                      <table className="table">
                        <thead>
                          <tr>
                            <th scope="col">Id</th>
                            <th scope="col">Nombre</th>
                            <th scope="col">Apellido</th>
                            <th scope="col">Dirección</th>
                            <th scope="col">Teléfono</th>
                          </tr>
                        </thead>
                        {!!store.entregas &&
                          store.entregas.map((entrega, i) => {
                            return (
                              <tbody>
                                <tr>
                                  <th scope="row" key={i}>
                                    {entrega.id}
                                  </th>
                                  <td>{entrega.nombre}</td>
                                  <td>{entrega.apellido}</td>
                                  <td>{entrega.direccion}</td>
                                  <td>{entrega.telefono}</td>
                                  <Link to="/">
                                    <button
                                      type="button"
                                      className="btn btn-success btn-lg mt-1"
                                    >
                                      Mapa
                                    </button>
                                  </Link>
                                </tr>
                              </tbody>
                            );
                          })}
                      </table>

                      <hr />
                      <div className="gap-3 d-inline-flex  justify-content-md-end text-center">
                       
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default DireccionesUsuario;
