import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Login from "./pages/Login";
import Me from './pages/Me';
import Register from './pages/Register';
import ProtectedRoute from './components/ProtectedRoute';
import './App.css'

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />
                <Route
                    path="/me"
                    element={
                        <ProtectedRoute>
                            <Me />
                        </ProtectedRoute>
                    }
                />
            </Routes>
        </BrowserRouter>
    );
}

export default App
