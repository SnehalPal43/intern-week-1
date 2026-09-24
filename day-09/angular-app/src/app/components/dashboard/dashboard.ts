import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { FacilityService } from '../../services/facility.service';
import { Facility } from '../../models/facility';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './dashboard.html',
  styleUrls: ['./dashboard.css']
})
export class DashboardComponent implements OnInit {
  facilities: Facility[] = [];
  filteredFacilities: Facility[] = [];
  searchTerm: string = '';
  sortBy: string = 'id';
  errorMessage: string = '';

  // Metrics
  totalFacilities: number = 0;
  activeFacilities: number = 0;

  // Selected Facility & History for Inspection
  selectedFacility: Facility | null = null;
  inspectionNotes: string = '';
  inspectionHistory: { facilityName: string; notes: string; date: string }[] = [];

  constructor(private facilityService: FacilityService) {}

  ngOnInit(): void {
    this.loadFacilities();
  }

  loadFacilities(): void {
    this.facilityService.getFacilities().subscribe({
      next: (data) => {
        this.facilities = data;
        this.filteredFacilities = data;
        this.calculateMetrics();
        this.sortFacilities();
      },
      error: (err) => {
        this.errorMessage = 'Failed to load facilities from API.';
        console.error('API Error:', err);
      }
    });
  }

  calculateMetrics(): void {
    this.totalFacilities = this.facilities.length;
    this.activeFacilities = this.facilities.filter(f => (f.status || 'Active') === 'Active').length;
  }

  filterFacilities(): void {
    const term = this.searchTerm.toLowerCase();
    this.filteredFacilities = this.facilities.filter(facility =>
      facility.name.toLowerCase().includes(term) ||
      facility.location.toLowerCase().includes(term)
    );
    this.sortFacilities();
  }

  sortFacilities(): void {
    this.filteredFacilities.sort((a, b) => {
      if (this.sortBy === 'name') {
        return a.name.localeCompare(b.name);
      } else {
        return a.id - b.id;
      }
    });
  }

  selectFacility(facility: Facility): void {
    this.selectedFacility = facility;
    this.inspectionNotes = '';
  }

  submitInspection(): void {
    if (this.selectedFacility && this.inspectionNotes.trim()) {
      this.inspectionHistory.unshift({
        facilityName: this.selectedFacility.name,
        notes: this.inspectionNotes,
        date: new Date().toLocaleString()
      });
      alert('Inspection submitted successfully!');
      this.inspectionNotes = '';
      this.selectedFacility = null;
    } else {
      alert('Please enter inspection notes before submitting.');
    }
  }
}
