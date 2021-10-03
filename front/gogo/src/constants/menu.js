import { adminRoot, UserRole } from './defaultValues';

const data = [
  {
    id: 'superAdministrador_dashboard',
    icon: 'iconsminds-library',
    label: 'Resumen',
    to: "/app/gogo/start",
    roles: [UserRole.SuperAdmin]
  },
  {
    id: 'superAdministrador_locales_comerciales',
    icon: 'iconsminds-library',
    label: 'Locales',
    to: "/app/locales_comerciales/locales",
    roles: [UserRole.SuperAdmin]
  },
  {
    id: 'superAdministrador_administradores',
    icon: 'iconsminds-library',
    label: 'Administradores',
    to: "/app/administradores_locales_comerciales/administradores",
    roles: [UserRole.SuperAdmin]
  },
  {
    id: 'administrador_categorias',
    icon: 'iconsminds-library',
    label: 'Categorias',
    to: 'https://gogo-react-docs.coloredstrategies.com/',
    newWindow: true,
    roles: [UserRole.AdminLocalComercial]
  },
  {
    id: 'administrador_productos',
    icon: 'iconsminds-library',
    label: 'Productos',
    to: 'https://gogo-react-docs.coloredstrategies.com/',
    newWindow: true,
    roles: [UserRole.AdminLocalComercial]
  },
  {
    id: 'administrador_ventas',
    icon: 'iconsminds-library',
    label: 'Ventas',
    to: 'https://gogo-react-docs.coloredstrategies.com/',
    newWindow: true,
    roles: [UserRole.AdminLocalComercial]
  },
  {
    id: 'administrador_tienda',
    icon: 'iconsminds-library',
    label: 'Tienda',
    to: 'https://gogo-react-docs.coloredstrategies.com/',
    newWindow: true,
    roles: [UserRole.AdminLocalComercial]
  },

];
export default data;
