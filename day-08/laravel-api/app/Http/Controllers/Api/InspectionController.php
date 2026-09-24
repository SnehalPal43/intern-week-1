<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\Inspection;
use Illuminate\Http\Request;

class InspectionController extends Controller
{
    public function index()
    {
        return response()->json(Inspection::with('facility')->get(), 200);
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'facility_id' => 'required|exists:facilities,id',
            'inspection_date' => 'required|date',
            'status' => 'required|string|max:255',
            'remarks' => 'nullable|string',
        ]);

        $inspection = Inspection::create($validated);
        return response()->json($inspection, 201);
    }

    public function show($id)
    {
        $inspection = Inspection::with('facility')->find($id);
        if (!$inspection) {
            return response()->json(['message' => 'Inspection not found'], 404);
        }
        return response()->json($inspection, 200);
    }

    public function update(Request $request, $id)
    {
        $inspection = Inspection::find($id);
        if (!$inspection) {
            return response()->json(['message' => 'Inspection not found'], 404);
        }

        $validated = $request->validate([
            'facility_id' => 'required|exists:facilities,id',
            'inspection_date' => 'required|date',
            'status' => 'required|string|max:255',
            'remarks' => 'nullable|string',
        ]);

        $inspection->update($validated);
        return response()->json($inspection, 200);
    }

    public function destroy($id)
    {
        $inspection = Inspection::find($id);
        if (!$inspection) {
            return response()->json(['message' => 'Inspection not found'], 404);
        }

        $inspection->delete();
        return response()->json(['message' => 'Inspection deleted successfully'], 200);
    }
}
