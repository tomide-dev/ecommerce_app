const API_URL = "http://localhost:5000";

// 🔐 LOGIN
export const login = async (form) => {
    try {
        const response = await fetch(`${API_URL}/auth/login`, {
            method: "POST",
            mode: "cors",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(form),
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.message || "Login failed");
        }

        return data;

    } catch (error) {
        console.error("LOGIN ERROR:", error);
        throw error;
    }
};


// 🛒 GET PRODUCTS (Protected Route)
export const getProducts = async (token) => {
    try {
        const response = await fetch(`${API_URL}/products`, {
            method: "GET",
            headers: {
                Authorization: `Bearer ${token}`, // 🔥 VERY IMPORTANT
            },
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error("Failed to fetch products");
        }

        return data;

    } catch (error) {
        console.error("GET PRODUCTS ERROR:", error);
        return []; // prevents crash
    }
};