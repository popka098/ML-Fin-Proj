import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Login from "./pages/Login";
import Me from './pages/Me';
import ProtectedRoute from './components/ProtectedRoute';
import './App.css'

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/login" element={<Login />} />
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
