const getState = ({ getStore, getActions, setStore }) => {
  return {
    store: {
      apiURL:
        "https://3001-marellanore-casinoborra-87u7eajyj8x.ws-us65.gitpod.io",
      token: null,
      message: null,
      user: {
        nombre: "",
        apellido: "",
        telefono: "",
        direccion: "",
        email: "",
        empresa_id: "",
      },
      empresa: {
        nombre: "",
        telefono: "",
        direccion: "",
        email: "",
      },
      casino: {
        nombre: "",
        telefono: "",
        direccion: "",
        email: "",
      },
      menus: [],
      entregas:[],
      infocasino:[],
      get_usuarios:[],
      get_empresa:[]
    },
    actions: {
      // Use getActions to call a function within a fuction
      exampleFunction: () => {
        getActions().changeColor(0, "green");
      },

      syncTokenFromSessionStore: () => {
        const token = sessionStorage.getItem("token");
        console.log("Application loaded");
        if (token && token != "" && token != undefined)
          setStore({ token: token });
      },
      register: async (nombre, apellido, telefono, direccion, email, password, empresa, navigate) => {
				const opts = {
					method: 'POST',
					headers: {
						'Content-Type': 'application/json'
					},
					body: JSON.stringify({
						'nombre': nombre,
						'apellido': apellido,
						'telefono': telefono,
						'direccion': direccion,
						'email': email,
						'password': password,
						'empresa_id': empresa
					})
				};
				await fetch('https://3001-marellanore-casinoborra-87u7eajyj8x.ws-us65.gitpod.io/api/register', opts)
					.then(response => response.json())
					.then((data) => {
						navigate('/login');
						console.log(data);
					})
					.catch((error) => {
						console.error(error);
					})
			},
      registroEmpresa: async (
        nombre,
        telefono,
        direccion,
        email,
        password,
        navigate
      ) => {
        const opts = {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            nombre: nombre,
            telefono: telefono,
            direccion: direccion,
            email: email,
            password: password,
          }),
        };
        await fetch(
          "https://3001-marellanore-casinoborra-87u7eajyj8x.ws-us65.gitpod.io/api/registro",
          opts
        )
          .then((response) => response.json())
          .then((data) => {
            navigate("/login-empresa");
            console.log(data);
          })
          .catch((error) => {
            console.error(error);
          });
      },
      registroCasino: async (
        nombre,
        telefono,
        direccion,
        email,
        password,
        navigate
      ) => {
        const opts = {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            nombre: nombre,
            telefono: telefono,
            direccion: direccion,
            email: email,
            password: password,
          }),
        };
        await fetch(
          "https://3001-marellanore-casinoborra-87u7eajyj8x.ws-us65.gitpod.io/api/registro-casino",
          opts
        )
          .then((response) => response.json())
          .then((data) => {
            navigate("/login-casino");
            console.log(data);
          })
          .catch((error) => {
            console.error(error);
          });
      },

      login: async (email, password, navigate) => {
        const opts = {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            email: email,
            password: password,
          }),
        };
        await fetch(
          "https://3001-marellanore-casinoborra-87u7eajyj8x.ws-us65.gitpod.io/api/login/user",
          opts
        )
          .then((response) => response.json())
          .then((data) => {
            navigate("/user-menu");
            console.log("This came from the backend", data);
            sessionStorage.setItem("token", data.access_token);
            setStore({ token: data.access_token });
            return true;
          })
          .catch((error) => {
            console.error(error);
          });
      },
      loginEmpresa: async (email, password, navigate) => {
        const opts = {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            email: email,
            password: password,
          }),
        };
        await fetch(
          "https://3001-marellanore-casinoborra-87u7eajyj8x.ws-us65.gitpod.io/api/login/empresa",
          opts
        )
          .then((response) => response.json())
          .then((data) => {
            navigate("/informacion-empresa");
            console.log("This came from the backend", data);
            sessionStorage.setItem("token", data.access_token);
            setStore({ token: data.access_token });
            return true;
          })
          .catch((error) => {
            console.error(error);
          });
      },
      loginCasino: async (email, password, navigate) => {
        const opts = {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            email: email,
            password: password,
          }),
        };
        await fetch(
          "https://3001-marellanore-casinoborra-87u7eajyj8x.ws-us65.gitpod.io/api/login/casino",
          opts
        )
          .then((response) => response.json())
          .then((data) => {
            navigate("/detalle-empresa");
            console.log("This came from the backend", data);
            sessionStorage.setItem("token", data.access_token);
            setStore({ token: data.access_token });
            return true;
          })
          .catch((error) => {
            console.error(error);
          });
      },
      logout: () => {
        sessionStorage.removeItem("token");
        console.log("Login Out");
        setStore({ token: null });
      },
      protectedData: async () => {
        // retrieve token form localStorage
        const token = sessionStorage.getItem("token");
        const response = await fetch(
          "https://3001-marellanore-casinoborra-87u7eajyj8x.ws-us65.gitpod.io/api/protected",
          {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
              Authorization: "Bearer " + token,
            },
          }
        );
        if (!response.ok)
          throw Error("There was a problem in the login request");
        const responseJson = await response.json();
        setStore(responseJson);
      },
      createMenu: async (
        dia,
        ensalada,
        principal,
        postre,
        bebida,
        navigate
      ) => {
        const opts = {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            dia: dia,
            ensalada: ensalada,
            principal: principal,
            postre: postre,
            bebida: bebida,
          }),
        };
        await fetch(
          "https://3001-marellanore-casinoborra-87u7eajyj8x.ws-us65.gitpod.io/api/dia/menus",
          opts
        )
          .then((response) => response.json())
          .then((data) => {
            navigate("/menu-casino");
            console.log(data);
          })
          .catch((error) => {
            console.error(error);
          });
      },

      //decisionalmuerzo
      decisionAlmuerzo: async (decision, userid) => {
        const opts = {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            usuario_id: userid,
            decision: decision,
          }),
        };
        await fetch(
          "https://3001-marellanore-casinoborra-87u7eajyj8x.ws-us65.gitpod.io/api/decision-almuerzo",
          opts
        )
          .then((response) => response.json())
          .then((data) => {
            console.log(data);
          })
          .catch((error) => {
            console.error(error);
          });
      },

      getMenus: async () => {
        try {
          const response = await fetch(
            "https://3001-marellanore-casinoborra-87u7eajyj8x.ws-us65.gitpod.io/api/dia/menus"
          );
          if (!response.ok) throw new Error("Error al consultar menús");
          const data = await response.json();

          setStore({
            menus: data,
          });
        } catch (error) {
          console.log(error);
        }
      },
      getDecision: async () => {
        try {
          const response = await fetch(
            "https://3001-marellanore-casinoborra-87u7eajyj8x.ws-us65.gitpod.io/api/usuario"
          );
          if (!response.ok) throw new Error("Error al consultar las entregas");
          const data = await response.json();

          setStore({
            entregas: data,
          });
        } catch (error) {
          console.log(error);
        }
      },
      getCasino: async () => {
        try {
          const response = await fetch(
            "https://3001-marellanore-casinoborra-87u7eajyj8x.ws-us65.gitpod.io/api/casino"
          );
          if (!response.ok) throw new Error("Error al consultar el casino");
          const data = await response.json();

          setStore({
            infocasino: data,
          });
        } catch (error) {
          console.log(error);
        }
      },
      getUsuarios: async () => {
        try {
          const response = await fetch(
            "https://3001-marellanore-casinoborra-87u7eajyj8x.ws-us65.gitpod.io/api/usuario"
          );
          if (!response.ok) throw new Error("Error al consultar los usuarios");
          const data = await response.json();

          setStore({
            get_usuarios: data,
          });
        } catch (error) {
          console.log(error);
        }
      },
      getEmpresa: async () => {
        try {
          const response = await fetch(
            "https://3001-marellanore-casinoborra-87u7eajyj8x.ws-us65.gitpod.io/api/empresa"
          );
          if (!response.ok) throw new Error("Error al consultar la empresa");
          const data = await response.json();

          setStore({
            get_empresa: data,
          });
        } catch (error) {
          console.log(error);
        }
      },
    },
  };
};

export default getState;
