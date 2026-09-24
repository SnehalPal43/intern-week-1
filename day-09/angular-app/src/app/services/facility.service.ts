import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Facility } from '../models/facility';

@Injectable({
  providedIn: 'root'
})
export class FacilityService {
  
  private apiUrl = 'http://127.0.0.1:8000/api/facilities';

  constructor(private http: HttpClient) {}

  getFacilities(): Observable<Facility[]> {
    return this.http.get<Facility[]>(this.apiUrl);
  }
}