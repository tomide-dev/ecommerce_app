import { useEffect, useState } from "react";
import { getProducts } from "../services/api";

function Products({ token }) {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        const fetchProducts = async () => {
            try {
                const data = await getProducts(token);
                console.log("PRODUCTS:", data);

                // Ensure it's always an array
                setProducts(Array.isArray(data) ? data : []);
            } catch (error) {
                console.error("ERROR:", error);
                setProducts([]);
            }
        };

        fetchProducts();
    }, [token]);

    return (
        <div>
            <h2>Products</h2>

            {products.length === 0 ? (
                <p>No products found or still loading...</p>
            ) : (
                products.map((p) => (
                    <div key={p.id}>
                        {p.name} - ${p.price}
                    </div>
                ))
            )}
        </div>
    );
}

export default Products;