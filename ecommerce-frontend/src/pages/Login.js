import { useState } from "react";
import { login } from "../services/api";

function Login({ setToken }) {
    const [form, setForm] = useState({ username: "", password: "" });

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await fetch("http://127.0.0.1:5000/auth/login", {
                method: "POST",
                mode: "cors",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(form),
            });

            const data = await response.json();
            console.log(data);

            if (data.token) {
                setToken(data.token);
            } else {
                alert("Login failed");
            }

        } catch (error) {
            console.error(error);
            alert("Connection error");
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input placeholder="Username" onChange={e => setForm({ ...form, username: e.target.value })} />
            <input type="password" placeholder="Password" onChange={e => setForm({ ...form, password: e.target.value })} />
            <button>Login</button>
        </form>
    );
}

export default Login;