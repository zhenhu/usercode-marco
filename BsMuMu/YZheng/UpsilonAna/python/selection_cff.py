import FWCore.ParameterSet.Config as cms

detailedDimuonTree = cms.EDFilter('ProbeTreeProducer',
    src = cms.InputTag("onia2MuMuPatTrkTrk", "DiMu"),
    variables = cms.PSet(
        pt = cms.string("pt"),
        y  = cms.string("rapidity"),
        eta  = cms.string("eta"),
        # mass = cms.string("mass"),
        mass = cms.string("userFloat('kinMass')"),
        m = cms.string("userFloat('kinMass')"),
        me = cms.string("userFloat('kinMassError')"),
        vProb = cms.string("userFloat('vProb')"),
        pvw8 = cms.string("userFloat('pvw8')"),
        pvw8Refit = cms.string("userFloat('pvw8Refit')"),
        charge = cms.string("charge"),
        isolation = cms.string("userFloat('Isolation')"),
        iso = cms.string("userFloat('Isolation20')"),
        docatrk = cms.string("userFloat('minDca')"),
        ntrk = cms.string("userInt('Ntrk')"),
        ntrkhp = cms.string("userInt('Ntrkhp')"),
        closetrk = cms.string("userInt('Ntrk20')"),
        ntrkhp20 = cms.string("userInt('Ntrkhp20')"),
        ntrk1sigma = cms.string("userInt('Ntrk1sigma')"),
        ntrk1isgmahp = cms.string("userInt('Ntrk1sigmahp')"),
        ntrk1sigma20 = cms.string("userInt('Ntrk1sigma20')"),
        ntrk1sigmahp20 = cms.string("userInt('Ntrk1sigmahp20')"),
        ntrk2sigma = cms.string("userInt('Ntrk2sigma')"),
        ntrk2isgmahp = cms.string("userInt('Ntrk2sigmahp')"),
        ntrk2sigma20 = cms.string("userInt('Ntrk2sigma20')"),
        ntrk2sigmahp20 = cms.string("userInt('Ntrk2sigmahp20')"),
        ntrk3sigma = cms.string("userInt('Ntrk3sigma')"),
        ntrk3isgmahp = cms.string("userInt('Ntrk3sigmahp')"),
        ntrk3sigma20 = cms.string("userInt('Ntrk3sigma20')"),
        ntrk3sigmahp20 = cms.string("userInt('Ntrk3sigmahp20')"),
        countTksOfPV = cms.string("userInt('countTksOfPV')"),
        countTksOfNoVtx = cms.string("userInt('countTksOfNoVtx')"),
        # vertexWeight = cms.string("userFloat('vertexWeight')"),
        sumPTPV = cms.string("userFloat('sumPTPV')"),
        sumPTNoVtx = cms.string("userFloat('sumPTNoVtx')"),
        sumNdofPV = cms.string("userFloat('sumNdofPV')"),
        sumNdofNoVtx = cms.string("userFloat('sumNdofNoVtx')"),
        dcaxy = cms.string("userFloat('DCAXY')"),
        maxdoca = cms.string("userFloat('DCA')"),
        ctauPV = cms.string("userFloat('ppdlPV')"),
        ctauErrPV = cms.string("userFloat('ppdlErrPV')"),
        cosAlphaXY = cms.string("userFloat('cosAlphaXY')"),
        cosa = cms.string("userFloat('cosAlpha3D')"),
        alpha = cms.string("userFloat('alpha')"),
        pvip = cms.string("userFloat('delta3d')"),
        pvips = cms.string("userFloat('delta3d')/userFloat('delta3dErr')"),
        delta3dErr = cms.string("userFloat('delta3dErr')"),
        PDGid = cms.string("userInt('momPDGId')"),
        chi2dof = cms.string("userFloat('vNChi2')"),
        highPurity1 = cms.string("userInt('highPurity1')"),
        highPurity2 = cms.string("userInt('highPurity2')"),
        fl3d = cms.string("userFloat('l3d')"),
        fls3d = cms.string("userFloat('l3dsig')"),
        pvlip = cms.string("userFloat('pvlip')"),
        pvlipErr = cms.string("userFloat('pvlipErr')"),
        lxy = cms.string("userFloat('lxy')"),
        lxysig = cms.string("userFloat('lxysig')"),

        m1pt = cms.string("daughter('muon1').pt"),
        m1eta = cms.string("daughter('muon1').eta"),
        mu1_phi = cms.string("daughter('muon1').phi"),
        mu1_charge = cms.string("daughter('muon1').charge"),
        mu1_nPixLayersWithMeasurement = cms.string("daughter('muon1').innerTrack.hitPattern.pixelLayersWithMeasurement"),
        mu1_nTrHits = cms.string("daughter('muon1').innerTrack.numberOfValidHits"),
        mu1_nChi2 = cms.string("daughter('muon1').innerTrack.normalizedChi2"),
        mu1_nMuSegs = cms.string("daughter('muon1').numberOfMatches('SegmentAndTrackArbitration')"),
        mu1_nMuSegsCln = cms.string("daughter('muon1').numberOfMatches('SegmentAndTrackArbitrationCleaned')"),
        mu1_dxy = cms.string("daughter('muon1').innerTrack.dxy"),
        mu1_dB = cms.string("daughter('muon1').dB"),
        mu1_dz = cms.string("daughter('muon1').innerTrack.dz"),
        mu1_R03sumPt = cms.string("daughter('muon1').isolationR03.sumPt"),
        mu1_R03emEt = cms.string("daughter('muon1').isolationR03.emEt"),
        mu1_R03hadEt = cms.string("daughter('muon1').isolationR03.hadEt"),
        mu1_R05sumPt = cms.string("daughter('muon1').isolationR05.sumPt"),
        mu1_R05emEt = cms.string("daughter('muon1').isolationR05.emEt"),
        mu1_R05hadEt = cms.string("daughter('muon1').isolationR05.hadEt"),
        mu1_numMatchedStations = cms.string("daughter('muon1').numberOfMatchedStations"),
        mu1_numberOfValidPixelHits = cms.string("daughter('muon1').innerTrack.hitPattern.numberOfValidPixelHits"),
        mu1_trackerLayersWithMeasurement = cms.string("daughter('muon1').innerTrack.hitPattern.trackerLayersWithMeasurement"),
        mu1_numberOfValidMuonHits = cms.string("daughter('muon1').globalTrack.hitPattern.numberOfValidMuonHits"),
        mu1_iso = cms.string("userFloat('isoMu1')"),
        m1iso = cms.string("userFloat('isoMu1_20')"),

        # BDT mu-id variables
        mu1_validFrac = cms.string("daughter('muon1').innerTrack.validFraction"),
        mu1_globalChi2 = cms.string("daughter('muon1').globalTrack.normalizedChi2"),
        mu1_chi2LocPos = cms.string("daughter('muon1').combinedQuality.chi2LocalPosition"),
        mu1_trkEHitsOut = cms.string("daughter('muon1').innerTrack.trackerExpectedHitsOuter.numberOfLostTrackerHits"),
        mu1_segComp = cms.string("userFloat('segComp1')"),
        mu1_glbTrackProb = cms.string("daughter('muon1').combinedQuality.glbTrackProbability"),
        mu1_chi2LocMom = cms.string("daughter('muon1').combinedQuality.chi2LocalMomentum"),
        mu1_trkVHits = cms.string("daughter('muon1').innerTrack.hitPattern.numberOfValidTrackerHits"),

        m2pt = cms.string("daughter('muon2').pt"),
        m2eta = cms.string("daughter('muon2').eta"),
        mu2_phi = cms.string("daughter('muon2').phi"),
        mu2_charge = cms.string("daughter('muon2').charge"),
        mu2_nPixLayersWithMeasurement = cms.string("daughter('muon2').innerTrack.hitPattern.pixelLayersWithMeasurement"),
        mu2_nTrHits = cms.string("daughter('muon2').innerTrack.numberOfValidHits"),
        mu2_nChi2 = cms.string("daughter('muon2').innerTrack.normalizedChi2"),
        mu2_nMuSegs = cms.string("daughter('muon2').numberOfMatches('SegmentAndTrackArbitration')"),
        mu2_nMuSegsCln = cms.string("daughter('muon2').numberOfMatches('SegmentAndTrackArbitrationCleaned')"),
        mu2_dxy = cms.string("daughter('muon2').innerTrack.dxy"),
        mu2_dB = cms.string("daughter('muon2').dB"),
        mu2_dz = cms.string("daughter('muon2').innerTrack.dz"),
        mu2_R03sumPt = cms.string("daughter('muon2').isolationR03.sumPt"),
        mu2_R03emEt = cms.string("daughter('muon2').isolationR03.emEt"),
        mu2_R03hadEt = cms.string("daughter('muon2').isolationR03.hadEt"),
        mu2_R05sumPt = cms.string("daughter('muon2').isolationR05.sumPt"),
        mu2_R05emEt = cms.string("daughter('muon2').isolationR05.emEt"),
        mu2_R05hadEt = cms.string("daughter('muon2').isolationR05.hadEt"),
        mu2_numMatchedStations = cms.string("daughter('muon2').numberOfMatchedStations"),
        mu2_numberOfValidPixelHits = cms.string("daughter('muon2').innerTrack.hitPattern.numberOfValidPixelHits"),
        mu2_trackerLayersWithMeasurement = cms.string("daughter('muon2').innerTrack.hitPattern.trackerLayersWithMeasurement"),
        mu2_numberOfValidMuonHits = cms.string("daughter('muon2').globalTrack.hitPattern.numberOfValidMuonHits"),
        mu2_iso = cms.string("userFloat('isoMu2')"),
        m2iso = cms.string("userFloat('isoMu2_20')"),

        # BDT mu-id variables
        mu2_validFrac = cms.string("daughter('muon2').innerTrack.validFraction"),
        mu2_globalChi2 = cms.string("daughter('muon2').globalTrack.normalizedChi2"),
        mu2_chi2LocPos = cms.string("daughter('muon2').combinedQuality.chi2LocalPosition"),
        mu2_trkEHitsOut = cms.string("daughter('muon2').innerTrack.trackerExpectedHitsOuter.numberOfLostTrackerHits"),
        mu2_segComp = cms.string("userFloat('segComp2')"),
        mu2_glbTrackProb = cms.string("daughter('muon2').combinedQuality.glbTrackProbability"),
        mu2_chi2LocMom = cms.string("daughter('muon2').combinedQuality.chi2LocalMomentum"),
        mu2_trkVHits = cms.string("daughter('muon2').innerTrack.hitPattern.numberOfValidTrackerHits"),

    ),
    flags = cms.PSet(
        mu1_Calo = cms.string("daughter('muon1').isCaloMuon"),
        mu1_GM = cms.string("daughter('muon1').isGlobalMuon"),
        mu1_GMPT = cms.string("daughter('muon1').isGlobalMuon && daughter('muon1').muonID('GlobalMuonPromptTight')"),
        mu1_LSOLPTT = cms.string("daughter('muon1').isTrackerMuon && daughter('muon1').muonID('TMLastStationOptimizedLowPtTight')"),
        mu1_TM = cms.string("daughter('muon1').isTrackerMuon"),
        mu1_GMPTKINK = cms.string("daughter('muon1').isGlobalMuon && daughter('muon1').muonID('GlobalMuonPromptTight') && daughter('muon1').muonID('GMTkKinkTight')"),
        mu1_GMPTOPTOBARRELLOWPT = cms.string("daughter('muon1').isGlobalMuon && daughter('muon1').muonID('GlobalMuonPromptTight') && daughter('muon1').muonID('TMLastStationOptimizedBarrelLowPtTight')"),
        mu1_TMOST = cms.string("daughter('muon1').isTrackerMuon && daughter('muon1').muonID('TMOneStationTight')"),
        mu1_TMLST = cms.string("daughter('muon1').isTrackerMuon && daughter('muon1').muonID('TMLastStationTight')"),
        mu1_TMOSAT = cms.string("daughter('muon1').isTrackerMuon && daughter('muon1').muonID('TMOneStationAngTight')"),
        mu1_TMLSAT = cms.string("daughter('muon1').isTrackerMuon && daughter('muon1').muonID('TMLastStationAngTight')"),        
        # mu1_Tight = cms.string("daughter('muon1').isTight"),
        mu1_HLT_DoubleMu2BsL3 = cms.string("!daughter('muon1').triggerObjectMatchesByFilter('hltDoubleMu2BsL3Filtered').empty()"),
        mu1_HLT_DoubleMu3BsL3 = cms.string("!daughter('muon1').triggerObjectMatchesByFilter('hltDoubleMu3BsL3Filtered').empty()"),
        mu1_HLT_DoubleMu2BarrelBsL3 = cms.string("!daughter('muon1').triggerObjectMatchesByFilter('hltDoubleMu2BarrelBsL3Filtered').empty()"),
        mu1_HLT_DoubleMu2Dimuon6BsL3 = cms.string("!daughter('muon1').triggerObjectMatchesByFilter('hltDoubleMu2Dimuon6BsL3Filtered').empty()"),
        mu1_HLT_VertexmumuFilterBs6 = cms.string("!daughter('muon1').triggerObjectMatchesByFilter('hltVertexmumuFilterBs6').empty()"),
        mu1_HLT_VertexmumuFilterBs4 = cms.string("!daughter('muon1').triggerObjectMatchesByFilter('hltVertexmumuFilterBs4').empty()"),
        mu1_HLT_VertexmumuFilterBs345 = cms.string("!daughter('muon1').triggerObjectMatchesByFilter('hltVertexmumuFilterBs345').empty()"),
        mu1_HLT_VertexmumuFilterBs3p545 = cms.string("!daughter('muon1').triggerObjectMatchesByFilter('hltVertexmumuFilterBs3p545').empty()"),
        mu1_HLT_VertexmumuFilterBs47 = cms.string("!daughter('muon1').triggerObjectMatchesByFilter('hltVertexmumuFilterBs47').empty()"),
        
        mu2_Calo = cms.string("daughter('muon2').isCaloMuon"),
        mu2_GM = cms.string("daughter('muon2').isGlobalMuon"),
        mu2_GMPT = cms.string("daughter('muon2').isGlobalMuon && daughter('muon2').muonID('GlobalMuonPromptTight')"),
        mu2_LSOLPTT = cms.string("daughter('muon2').isTrackerMuon && daughter('muon2').muonID('TMLastStationOptimizedLowPtTight')"),
        mu2_TM = cms.string("daughter('muon2').isTrackerMuon"),
        mu2_GMPTKINK = cms.string("daughter('muon2').isGlobalMuon && daughter('muon2').muonID('GlobalMuonPromptTight') && daughter('muon2').muonID('GMTkKinkTight')"),
        mu2_GMPTOPTOBARRELLOWPT = cms.string("daughter('muon2').isGlobalMuon && daughter('muon2').muonID('GlobalMuonPromptTight') && daughter('muon2').muonID('TMLastStationOptimizedBarrelLowPtTight')"),
        mu2_TMOST = cms.string("daughter('muon2').isTrackerMuon && daughter('muon2').muonID('TMOneStationTight')"),
        mu2_TMLST = cms.string("daughter('muon2').isTrackerMuon && daughter('muon2').muonID('TMLastStationTight')"),
        mu2_TMOSAT = cms.string("daughter('muon2').isTrackerMuon && daughter('muon2').muonID('TMOneStationAngTight')"),
        mu2_TMLSAT = cms.string("daughter('muon2').isTrackerMuon && daughter('muon2').muonID('TMLastStationAngTight')"),
        # mu2_Tight = cms.string("daughter('muon2').isTight"),
        mu2_HLT_DoubleMu2BsL3 = cms.string("!daughter('muon2').triggerObjectMatchesByFilter('hltDoubleMu2BsL3Filtered').empty()"),
        mu2_HLT_DoubleMu3BsL3 = cms.string("!daughter('muon2').triggerObjectMatchesByFilter('hltDoubleMu3BsL3Filtered').empty()"),
        mu2_HLT_DoubleMu2BarrelBsL3 = cms.string("!daughter('muon2').triggerObjectMatchesByFilter('hltDoubleMu2BarrelBsL3Filtered').empty()"),
        mu2_HLT_DoubleMu2Dimuon6BsL3 = cms.string("!daughter('muon2').triggerObjectMatchesByFilter('hltDoubleMu2Dimuon6BsL3Filtered').empty()"),
        mu2_HLT_VertexmumuFilterBs6 = cms.string("!daughter('muon2').triggerObjectMatchesByFilter('hltVertexmumuFilterBs6').empty()"),
        mu2_HLT_VertexmumuFilterBs4 = cms.string("!daughter('muon2').triggerObjectMatchesByFilter('hltVertexmumuFilterBs4').empty()"),
        mu2_HLT_VertexmumuFilterBs345 = cms.string("!daughter('muon2').triggerObjectMatchesByFilter('hltVertexmumuFilterBs345').empty()"),
        mu2_HLT_VertexmumuFilterBs3p545 = cms.string("!daughter('muon2').triggerObjectMatchesByFilter('hltVertexmumuFilterBs3p545').empty()"),
        mu2_HLT_VertexmumuFilterBs47 = cms.string("!daughter('muon2').triggerObjectMatchesByFilter('hltVertexmumuFilterBs47').empty()")
    ),
    ignoreExceptions = cms.bool(True),
    addRunLumiInfo = cms.bool(True),
    filter = cms.bool(True),
)

def selection(process, GlobalTag="GR_R_38X_V8::All", MC=False, SelectionTrigger="hltL1DoubleMuOpenTightL1Filtered"):
#    process.load("Configuration.StandardSequences.MagneticField_cff")
#    process.load("Configuration.StandardSequences.Geometry_cff")
#    process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#    process.load("Configuration.StandardSequences.Reconstruction_cff")
#    process.GlobalTag.globaltag = cms.string(GlobalTag)
    process.load("FWCore.MessageService.MessageLogger_cfi")
    process.options = cms.untracked.PSet(
        wantSummary = cms.untracked.bool(True),
        # SkipEvent = cms.untracked.vstring('ProductNotFound'),
        fileMode = cms.untracked.string('NOMERGE')
    )
    process.MessageLogger.cerr.FwkReport.reportEvery = 100

    process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring()
    )

    process.primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
        vertexCollection = cms.InputTag('offlinePrimaryVertices'),
        minimumNDOF = cms.uint32(4),
        maxAbsZ = cms.double(25),	
        maxd0 = cms.double(2)	
    )

    if MC:
        process.triggerSelection = cms.EDFilter( "TriggerResultsFilter",
            triggerConditions = cms.vstring(
                'HLT_DoubleMu*Dimuon*'
            ),
            hltResults = cms.InputTag( "TriggerResults", "", "HLT" ),
            l1tResults = cms.InputTag( "" ),
            l1tIgnoreMask = cms.bool( False ),
            l1techIgnorePrescales = cms.bool( False ),
            daqPartitions = cms.uint32( 1 ),
            throw = cms.bool( True )
        )
    else:
        process.triggerSelection = cms.EDFilter( "TriggerResultsFilter",
            triggerConditions = cms.vstring(
                'HLT_DoubleMu3_4_Dimuon5_Bs_Central_v2',
                'HLT_DoubleMu3_4_Dimuon5_Bs_Central_v3',
                'HLT_DoubleMu3_4_Dimuon5_Bs_Central_v4',
                'HLT_DoubleMu3_4_Dimuon5_Bs_Central_v5',
                'HLT_DoubleMu3p5_4_Dimuon5_Bs_Central_v2',
                'HLT_DoubleMu3p5_4_Dimuon5_Bs_Central_v3',
                'HLT_DoubleMu3p5_4_Dimuon5_Bs_Central_v4',
                'HLT_DoubleMu3p5_4_Dimuon5_Bs_Central_v5',
                'HLT_DoubleMu4_Dimuon7_Bs_Forward_v2',
                'HLT_DoubleMu4_Dimuon7_Bs_Forward_v3',
                'HLT_DoubleMu4_Dimuon7_Bs_Forward_v4',
                'HLT_DoubleMu4_Dimuon7_Bs_Forward_v5'
            ),
            hltResults = cms.InputTag( "TriggerResults", "", "HLT" ),
            l1tResults = cms.InputTag( "" ),
            l1tIgnoreMask = cms.bool( False ),
            l1techIgnorePrescales = cms.bool( False ),
            daqPartitions = cms.uint32( 1 ),
            throw = cms.bool( True )
        )

    process.detailedDimuonTree = detailedDimuonTree

    process.detailedDimuonTreePath = cms.Path(
        process.triggerSelection *
        process.detailedDimuonTree
    )

    process.TFileService = cms.Service("TFileService", fileName = cms.string("selection_test.root"))

