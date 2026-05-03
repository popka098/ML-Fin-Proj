import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Index from './pages/Index';
import Login from "./pages/Login";
import Me from './pages/Me';
import Register from './pages/Register';

import ProtectedRoute from './components/ProtectedRoute';
import Header from './components/Header';

import './App.css'

function App() {
    return (
            <BrowserRouter>
                <Header />
                <Routes>
                    <Route
                        path="/"
                        element={
                            <ProtectedRoute>
                                <Index />
                            </ProtectedRoute>
                        }
                    />
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
