
// INTERFACES que debes utilizar durante las peticiones
// al backend, estas interfaces representan la estructura de los datos
// utilizalas para estructurar correctamente las peticiones, fetch, axios etc
// manten los datos bien typeados 

// Prefijo de los endpoints para los actores economicos => api/v1/actorEconomico/ (Aqui va la parte de la ruta para lo que vas a hacer crear o editar)/ ( aca los parametros que requiere la ruta)

export interface IActorEconomicoResponse{
    id : number;
    nombre : string;
    solicitud : string;
    actividad_principal_CNAE_id:string; //FK
    denominacion_id: number; //FK
    tipo_sujeto_id:number; //FK
    actividad_economica_principal_id:number; //FK
    solicitante_id:number; //FK
    tipo_mypime_id:number;//FK
    sector_economico_id:number;//FK
    origen_id:number; //FK
    telefono: string;
    correo_representante:string;
    domicilio_social : string;
    cantidad_socios: number;
    cantidad_trabajadores: number;
    cantidad_estatales: number;
    cantidad_TPCP: number;
    cantidad_CNAA: number;
    cantidad_desempleados: number;
    cantidad_otros_origenes: number;
    cantidad_ocupados: number;
    pdl : string;
    inscrito_registro_mercantil: boolean;
    folio_inscripcion:string;
    hoja_inscripcion: string;
    fecha_incripcion:string;
    is_exportador:boolean;
    is_incubado_en_parque_cientifico:boolean;
    desistimiento_con_carta_de_socios:boolean;
    is_disuelta:boolean;
    is_inactiva:boolean;
    tipoMypime:ITipoMIPYMEResponse;
    tipoSujeto: ITipoSujetoResponse;
    solicitante: ISolicitanteResponse;
    actividadEconomicaPrincipalCNAE: IActividadPrincipalCNAEResponse;
    actividadEconomica: IActividadEconomicaResponse;
    sectorEconomico: ISectorEconomicoResponse;
    denominacion: IDenominacionResponse;
    origen: IOrigenResponse;
}

export interface ISolicitanteResponse{
    id:number;
    nombre:string;
    segundo_nombre:string | null;
    apellido_paterno:string;
    apellido_materno:string;
    telefono:string ;
    correo: string | null;
    carnet:string;
    tomo:string;
    folio:string
    fecha_nacimiento:string;
    genero:string;
    direccion:string;
    tipo_mipyme_id:number; //FK
    TipoMypime: ITipoMIPYMEResponse;

}

// Prefijo de los endpoints para los tipos de mipymes => api/v1/tiposMiPymes/
export interface ITipoMIPYMEResponse{
    id: number;
    nombre: string;
    descripcion:string;
    
}
// Prefijo de los endpoints para las denominaciones => api/v1/denominaciones/

export interface IDenominacionResponse {
    id: number;
    nombre: string;
    descripcion : string;
    created_at: string;
    updated_at: string;
}

// Prefijo de los endpoints para las actividades econominas => api/v1/actividadEconomica/
export interface IActividadEconomicaResponse{
    id: number;
    nombre: string;
    codigo: string;
    descripcion: string;
    created_at:string;
    updated_at:string;
}

// Prefijo de los endpoints para las actividades principales del CNAE => api/v1/actividadPrincipal/

export interface IActividadPrincipalCNAEResponse{
    id: number;
    nombre: string;
    descripcion:string;
}


// Prefijo de los endpoints para los sectores economicos => api/v1/sectorEconomico/
export interface ISectorEconomicoResponse{
    id: number;
    nombre: string;
    descripcion: string;
}

// Prefijo de los endpoints para los tipos de sujetos => api/v1/sectorEconomico/
export interface ITipoSujetoResponse{
    id: number;
    nombre: string;
    descripcion: string;
    created_at: string;
    updated_at: string;
}
// Prefijo de los enpoints para los origenes => ap1/v1/origen/
export interface IOrigenResponse{
    id:number;
    nombre:string;
    descripcion:string;
    created_at:string;
    updated_at:string;
}

